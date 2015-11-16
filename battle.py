import re
import achievements
import printing

class summary:
    def __init__(self, chat_json, current_boss):
        """
        Construct a battle summary based on the party chat.
        """
        attack = re.compile("\`([a-zA-z0-9 ]+) attacks ([a-zA-z' ]+) for ([0-9\.]+) "
                    "damage, [a-zA-z' ]+ attacks party for ([0-9\.]+) damage")
        # Construct dictionary which stores the data for achievements and table.
        self.dmgDict = {}
        for message in chat_json:
            if message["uuid"] == "system" and attack.match(message["text"]):
                player, boss, damage_given, damage_taken = \
                    attack.search(message["text"]).groups()
                if boss == current_boss:
                    if player in self.dmgDict.keys():
                        self.dmgDict[player]['damageGiven'] += float(damage_given)
                        self.dmgDict[player]['damageTaken'] += float(damage_taken)
                        dg = self.dmgDict[player]['damageGiven']
                        dt = self.dmgDict[player]['damageTaken']
                        self.dmgDict[player]['kd'] = dg / max(dt, 1)
                        self.dmgDict[player]['nrAttacks'] += 1
                    else:
                        self.dmgDict[player] = {
                            'bossName': boss,
                            'damageGiven': float(damage_given),
                            'damageTaken': float(damage_taken),
                            'kd': float(damage_given)/max(float(damage_taken), 1),
                            'maxAttack': float(damage_given),
                            'maxFU': float(damage_taken),
                            'nrAttacks': 1
                        }
                    if float(damage_given) > self.dmgDict[player]['maxAttack']:
                        self.dmgDict[player]['maxAttack'] = float(damage_given)
                    if float(damage_taken) > self.dmgDict[player]['maxFU']:
                        self.dmgDict[player]['maxFU'] = float(damage_taken)
        
        # Award achievements
        self.achmts = achievements.get_achievement_dict(self.dmgDict)
    
    def __repr__(self):
        string = printing.title("Battle Summary", 1) + '\n'
        summary_table = printing.table(['User', 'Damage given', 'Damage taken', 'K/D ratio'])
        for key, value in self.dmgDict.iteritems():
            summary_table.add_row([key, \
                "{:.1f}".format(value["damageGiven"]), \
                "{:.1f}".format(value["damageTaken"]), \
                "{:.1f}".format(value["kd"])])
        string += repr(summary_table) + '\n\n'
        
        string += printing.title("Achievements", 2) + '\n'
        for key in self.achmts.iterkeys():
            string += repr(key) + '\n'
            
        return string
