import re

re_player = "[\w ]+"
re_quest = "[\w', ]+"
re_num = "[\d\.]+"
re_attack = re.compile("\`(" + re_player + ") "
            "attacks (" + re_quest + ") for (" + re_num + ") "
            "damage, " + re_quest + " attacks party for (" + re_num + ") damage.\`")
re_find = re.compile("\`(" + re_player + ") found (" + re_num + ") "
            "(" + re_quest + ").\`")
re_complete_boss = re.compile("\`You defeated (" + re_quest + ")! Questing "
            "party members receive the rewards of victory.\`")
re_complete_collect = re.compile("\`All items found! Party has received their "
            "rewards.\`")

def damage_dict(messages):
    dmgDict = {}
    for message in messages:
        if message["uuid"] == "system" and re_attack.match(message["text"]):
            player, boss, damage_given, damage_taken = \
                re_attack.search(message["text"]).groups()
            if player in dmgDict.keys():
                dmgDict[player]['damageGiven'] += float(damage_given)
                dmgDict[player]['damageTaken'] += float(damage_taken)
                dg = dmgDict[player]['damageGiven']
                dt = dmgDict[player]['damageTaken']
                dmgDict[player]['kd'] = dg / max(dt, 1)
                dmgDict[player]['nrAttacks'] += 1
            else:
                dmgDict[player] = {
                    'bossName': boss,
                    'damageGiven': float(damage_given),
                    'damageTaken': float(damage_taken),
                    'kd': float(damage_given)/max(float(damage_taken), 1),
                    'maxAttack': float(damage_given),
                    'maxFU': float(damage_taken),
                    'nrAttacks': 1
                }
            if float(damage_given) > dmgDict[player]['maxAttack']:
                dmgDict[player]['maxAttack'] = float(damage_given)
            if float(damage_taken) > dmgDict[player]['maxFU']:
                dmgDict[player]['maxFU'] = float(damage_taken)
    return dmgDict
