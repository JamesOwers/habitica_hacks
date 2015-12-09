import questutils
import achievements
import printing

def get_quest_messages(chat_json, quest):
    """
    Retrieve chat messages relating to a quest. Also return the type of quest "
    and the quest text.
    Generates a summary for the nth quest; quest=0 meaning the current quest.
    Quest text is the text to search for in the party chat. This is either
    the display name of the boss (accessed via content.quests.key.boss.name)
    or for a collect quest it's the name of item to be collected (accessed
    via content.quests.key.collect.key2.text). I think you might have to
    guess what key2 is, but it's probably the only entry under collect.
    """
    # Quest end messages I've seen so far are of the form:
    # - You defeated X! Questing party members receive the rewards of victory.
    #   (boss quest)
    # - All items found! Party has received their rewards. (collect quest)
    
    messages = []
    i=0
    quest_type = False
    quest_text = False
    
    for message in chat_json:
        if message["uuid"] == "system":
            if (questutils.re_complete_boss.match(message["text"]) or
                questutils.re_complete_collect.match(message["text"])):
                if i < quest:
                    i+=1
                else:
                    break
            elif questutils.re_attack.match(message["text"]):
                player, boss, damage_given, damage_taken = \
                    questutils.re_attack.search(message["text"]).groups()
                if i==quest:
                    quest_type = "boss"
                    quest_text = boss
                    messages.append(message)
            elif questutils.re_find.match(message["text"]):
                player, num, item = \
                    questutils.re_find.search(message["text"]).groups()
                if i==quest:
                    quest_type = "collect"
                    quest_text = item
                    messages.append(message)
        else:
            # Collect all non-system messages
            messages.append(message)
    return messages, quest_type, quest_text

def generate_table(messages, quest_type):
    if quest_type == "boss":
        dmgDict = questutils.damage_dict(messages)
        table = printing.table(['User', 'Damage given', 'Damage taken',
            'Attacks', 'K/D ratio'])
        for key, value in dmgDict.iteritems():
            table.add_row([key,
                "{:.1f}".format(value["damageGiven"]),
                "{:.1f}".format(value["damageTaken"]),
                "{:.0f}".format(value["nrAttacks"]),
                "{:.1f}".format(value["kd"])])
            
    elif quest_type == "collect":
        table = "Summary table not yet implemented for collect quests."
    else:
        table = "Error: Summary table not yet implemented for this type of " \
            "quest. Are you sure you're in a quest?"
    
    return table

def print_progress(habitica_content, party_info):
    if "quest" in party_info and party_info["quest"]:
        # Print status e.g. current boss and its health.
        print printing.title("Quest Status", 2)
        quest_key = party_info["quest"]["key"]
        quest_info = habitica_content["quests"][quest_key]
        if party_info["quest"]["active"]:
            if "boss" in quest_info:
                boss_hp = party_info["quest"]["progress"]["hp"]
                boss_max_hp = quest_info["boss"]["hp"]
                boss_name = quest_info["boss"]["name"]
                print 'Boss: {}'.format(boss_name)
                sys.stdout.write('{}/{} '.format(int(round(boss_hp)), boss_max_hp))
                sys.stdout.write(printing.progress_bar(boss_hp, boss_max_hp, boss_health_bar_width))
                sys.stdout.write('\n\n')
                print quest.summary(messages, boss_name)
            elif "collect" in quest_info:
                print "Collecting items..."
        else:
            print "Waiting for members.\n"
    
def print_table(messages, quest_type):
    string = printing.title("Quest Summary", 1) + '\n'
    string += repr(generate_table(messages, quest_type)) + '\n\n'
    print string
