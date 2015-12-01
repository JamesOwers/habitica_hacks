import battle
import operator
import re

class achievement(object):
    def __init__(self, messages, quest_type):
        self.weight = -1
        self.title = "Achievement"
        self.explanation = "Best player"
        self.player = "Player 1"
        self.quotation = False
    def get_weight(self):
        return self.weight
    def get_title(self):
        return self.title
    def get_explanation(self):
        return self.explanation
    def get_player(self):
        return self.player
    def get_quotation(self):
        return self.quotation
    def __repr__(self):
        return "*{}*: {} ({})".format(self.get_title(), self.get_player(), \
            self.get_explanation())
        
class best_player(achievement):
    def __init__(self, m, t):
        super(best_player, self).__init__(m,t)
        if t == "boss":
            dmgDict = battle.damage_dict(m)
            self.title = "Best player"
            # Max damage ratio
            kds = {key: value["kd"] for key, value in dmgDict.iteritems()}
            self.player, self.weight = max(kds.iteritems(), key=operator.itemgetter(1))
            self.explanation = "{:.1f} K/D ratio".format(self.weight)
        
class damp_squib(achievement):
    def __init__(self, m, t):
        super(damp_squib, self).__init__(m,t)
        if t == "boss":
            dmgDict = battle.damage_dict(m)
            self.title = "Damp Squib"
            # Min damage ratio
            kds = {key: value["kd"] for key, value in dmgDict.iteritems()}
            self.player, self.kd = min(kds.iteritems(), key=operator.itemgetter(1))
            self.explanation = "{:.1f} K/D ratio".format(self.kd)
            self.weight = 1./(self.kd + 1)
        
class bravery(achievement):
    def __init__(self, m, t):
        super(bravery, self).__init__(m,t)
        if t == "boss":
            dmgDict = battle.damage_dict(m)
            self.title = "Bravery"
            # Max number of attacks
            attacks = {key: value["nrAttacks"] for key, value in dmgDict.iteritems()}
            self.player, self.num = max(attacks.iteritems(), key=operator.itemgetter(1))
            other_players = {key: value["nrAttacks"] for key, value in dmgDict.iteritems() \
                if value["nrAttacks"] == self.num}
            self.weight = self.num if len(other_players) == 1 else -1
            self.explanation = "{} attacks".format(self.num)
        
class coward(achievement):
    def __init__(self, m, t):
        super(coward, self).__init__(m,t)
        if t == "boss":
            dmgDict = battle.damage_dict(m)
            self.title = "Coward"
            # Min number of attacks
            attacks = {key: value["nrAttacks"] for key, value in dmgDict.iteritems()}
            self.player, self.num = min(attacks.iteritems(), key=operator.itemgetter(1))
            other_players = {key: value["nrAttacks"] for key, value in dmgDict.iteritems() \
                if value["nrAttacks"] == self.num}
            self.weight = 100 if len(other_players) == 1 else -1
            self.explanation = "only {} attacks".format(self.num)
        
class warrior(achievement):
    def __init__(self, m, t):
        super(warrior, self).__init__(m,t)
        if t == "boss":
            dmgDict = battle.damage_dict(m)
            self.title = "The Warrior"
            # Max HP in one attack
            attacks = {key: value["maxAttack"] for key, value in dmgDict.iteritems()}
            self.player, self.weight = max(attacks.iteritems(), key=operator.itemgetter(1))
            self.explanation = "{:.1f} HP in one attack".format(self.weight)
            for message in m:
                if battle.attack.match(message["text"]):
                    player, _, damage_given, _ = battle.attack.search(message["text"]).groups()
                    if player == self.player and float(damage_given) == self.weight:
                        self.quotation = get_relevant_quotation(message["id"], m)
                        break
            else:
                self.quotation = ("Couldn't find the message!", "wtf")
        
class weakling(achievement):
    def __init__(self, m, t):
        super(weakling, self).__init__(m,t)
        if t == "boss":
            dmgDict = battle.damage_dict(m)
            self.title = "The Weakling"
            # Weakest maximum attack
            attacks = {key: value["maxAttack"] for key, value in dmgDict.iteritems()}
            self.player, self.hp = min(attacks.iteritems(), key=operator.itemgetter(1))
            self.explanation = "{:.1f} HP maximum attack".format(self.hp)
            self.weight = 1./(self.hp + 1)
            for message in m:
                if battle.attack.match(message["text"]):
                    player, _, damage_given, _ = battle.attack.search(message["text"]).groups()
                    if player == self.player and float(damage_given) == self.hp:
                        self.quotation = get_relevant_quotation(message["id"], m)
                        break
            else:
                self.quotation = ("Couldn't find the message!", "wtf")
        
class useless(achievement):
    def __init__(self, m, t):
        super(useless, self).__init__(m,t)
        if t == "boss":
            dmgDict = battle.damage_dict(m)
            self.title = "Useless"
            # Min damage dealt
            attacks = {key: value["damageGiven"] for key, value in dmgDict.iteritems()}
            self.player, self.hp = min(attacks.iteritems(), key=operator.itemgetter(1))
            self.explanation = "{:.1f} HP total attack".format(self.hp)
            self.weight = 1./(self.hp + 1)
        
class friendly_fire(achievement):
    def __init__(self, m, t):
        super(friendly_fire, self).__init__(m,t)
        if t == "boss":
            dmgDict = battle.damage_dict(m)
            self.title = "Friendly Fire"
            # Max single damage dealt to group
            FUs = {key: value["maxFU"] for key, value in dmgDict.iteritems()}
            self.player, self.weight = max(FUs.iteritems(), key=operator.itemgetter(1))
            self.explanation = "{:.1f} HP taken from group in one day".format(self.weight)
            for message in m:
                if battle.attack.match(message["text"]):
                    player, _, _, damage_taken = battle.attack.search(message["text"]).groups()
                    if player == self.player and float(damage_taken) == self.weight:
                        self.quotation = get_relevant_quotation(message["id"], m)
                        break
            else:
                self.quotation = ("Couldn't find the message!", "wtf")
            
        
class liability(achievement):
    def __init__(self, m, t):
        super(liability, self).__init__(m,t)
        if t == "boss":
            dmgDict = battle.damage_dict(m)
            self.title = "Liability"
            # Max total damage dealt to group
            FUs = {key: value["damageTaken"] for key, value in dmgDict.iteritems()}
            self.player, self.weight = max(FUs.iteritems(), key=operator.itemgetter(1))
            self.explanation = "{:.1f} HP total taken from group".format(self.weight)
        
class safe_bet(achievement):
    def __init__(self, m, t):
        super(safe_bet, self).__init__(m,t)
        if t == "boss":
            dmgDict = battle.damage_dict(m)
            self.title = "Safe Bet"
            # Min total damage dealt to group
            FUs = {key: value["damageTaken"] for key, value in dmgDict.iteritems()}
            self.player, self.hp = min(FUs.iteritems(), key=operator.itemgetter(1))
            self.explanation = "only {:.1f} HP total taken from group".format(self.hp)
            other_players = {key: value["damageTaken"] for key, value in dmgDict.iteritems() \
                if value["damageTaken"] == self.hp}
            self.weight = 1./(self.hp + 1) if len(other_players) == 1 else -1

def get_achievements(m,t):
    """
    Get list of achievements for quest of type t using messages m.
    """
    achmts = [best_player(m,t),
        bravery(m,t),
        coward(m,t),
        damp_squib(m,t),
        warrior(m,t),
        weakling(m,t),
        useless(m,t),
        friendly_fire(m,t),
        liability(m,t),
        safe_bet(m,t)]
    return [a for a in achmts if a.get_weight() >= 0]

def get_relevant_quotation(messageid, messages):
    message = False
    for m in messages[::-1]:
        if m["id"] == messageid:
            message = m
            re_message = re.compile("\`(\w+)")
            relevant_info = re_message.search(m["text"]).group(1)
        elif message:
            re_message = re.compile(relevant_info, re.I)
            if m["uuid"] == "system" and re_message.match(m["text"]):
                return False
            if ((m["uuid"] != "system") and
                (re_message.match(m["text"]) or re_message.match(m["user"]))):
                return (m["text"], m["user"])
    else:
        return False

    
