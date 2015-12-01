import battle
import achievements
import printing

class summary:
    def __init__(self, chat_json, quest_text):
        """
        Construct a battle summary based on the party chat.
        Quest text is the text to search for in the party chat. This is either
        the display name of the boss (accessed via content.quests.key.boss.name)
        or for a collect quest it's the name of item to be collected (accessed
        via content.quests.key.collect.key2.text). I think you might have to
        guess what key2 is, but it's probably the only entry under collect.
        """
        # Find relevant messages
        messages = []
        quest_type = False
        for message in chat_json:
            if message["uuid"] == "system":
                if battle.attack.match(message["text"]):
                    player, boss, damage_given, damage_taken = \
                        battle.attack.search(message["text"]).groups()
                    if boss == quest_text:
                        quest_type = "boss"
                        messages.append(message)
                    else:
                        break
                elif battle.find.match(message["text"]):
                    player, found, item = \
                        battle.find.search(message["text"]).groups()
                    if item == quest_text:
                        quest_type = "collect"
                        messages.append(message)
                    else:
                        break
            else:
                messages.append(message)

        # Generate table
        self.summary_table = self.generate_table(messages, quest_type)
        
        # Award achievements
        self.achmts = achievements.get_achievements(messages, quest_type)

    def generate_table(self, messages, quest_type):
        if quest_type == "boss":
            dmgDict = battle.damage_dict(messages)
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
            table = "Summary table not yet implemented for this type of quest."
        
        return table
    
    def __repr__(self):
        string = printing.title("Quest Summary", 1) + '\n'
        string += repr(self.summary_table) + '\n\n'
        
        string += printing.title("Achievements", 2) + '\n'
        for achmt in self.achmts:
            string += repr(achmt) + '  \n'
            if achmt.get_quotation():
                q, name = achmt.get_quotation()
                string += '\t    "' + q + '" - ' + name + '  \n'
            
        return string
