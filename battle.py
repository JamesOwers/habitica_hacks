import re

re_player = "[\w ]+"
re_quest = "[\w', ]+"
re_num = "[\d\.]+"
attack = re.compile("\`(" + re_player + ") "
            "attacks (" + re_quest + ") for (" + re_num + ") "
            "damage, " + re_quest + " attacks party for (" + re_num + ") damage.\`")
find = re.compile("\`(" + re_player + ") found (" + re_num + ") "
            "(" + re_quest + ").\`")

def damage_dict(messages):
    dmgDict = {}
    for message in messages:
        if message["uuid"] == "system" and attack.match(message["text"]):
            player, boss, damage_given, damage_taken = \
                attack.search(message["text"]).groups()
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
