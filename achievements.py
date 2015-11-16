import operator

class achievement(object):
    def __init__(self, dmgDict):
        self.weight = 0
        self.title = "Achievement"
        self.explanation = "Best player"
        self.player = "Player 1"
    def get_weight(self):
        return self.weight
    def get_title(self):
        return self.title
    def get_explanation(self):
        return self.explanation
    def get_player(self):
        return self.player
    def __repr__(self):
        return "*{}*: {} ({})".format(self.get_title(), self.get_player(), \
            self.get_explanation())
        
class best_player(achievement):
    def __init__(self, dmgDict):
        super(best_player, self).__init__(dmgDict)
        self.title = "Best player"
        # Max damage ratio
        kds = {key: value["kd"] for key, value in dmgDict.iteritems()}
        self.player, self.kd = max(kds.iteritems(), key=operator.itemgetter(1))
    def get_explanation(self):
        return "{:.1f} K/D ratio".format(self.kd)
        
class damp_squib(achievement):
    def __init__(self, dmgDict):
        super(damp_squib, self).__init__(dmgDict)
        self.title = "Damp Squib"
        # Min damage ratio
        kds = {key: value["kd"] for key, value in dmgDict.iteritems()}
        self.player, self.kd = min(kds.iteritems(), key=operator.itemgetter(1))
    def get_explanation(self):
        return "{:.1f} K/D ratio".format(self.kd)
        
class bravery(achievement):
    def __init__(self, dmgDict):
        super(bravery, self).__init__(dmgDict)
        self.title = "Bravery"
        # Max number of attacks
        attacks = {key: value["nrAttacks"] for key, value in dmgDict.iteritems()}
        self.player, self.num = max(attacks.iteritems(), key=operator.itemgetter(1))
    def get_explanation(self):
        return "{:.1f} attacks".format(self.num)
        
class coward(achievement):
    def __init__(self, dmgDict):
        super(coward, self).__init__(dmgDict)
        self.title = "Coward"
        # Min number of attacks
        attacks = {key: value["nrAttacks"] for key, value in dmgDict.iteritems()}
        self.player, self.num = min(attacks.iteritems(), key=operator.itemgetter(1))
    def get_explanation(self):
        return "only {:.1f} attacks".format(self.num)
        
class warrior(achievement):
    def __init__(self, dmgDict):
        super(warrior, self).__init__(dmgDict)
        self.title = "The Warrior"
        # Max HP in one attack
        attacks = {key: value["maxAttack"] for key, value in dmgDict.iteritems()}
        self.player, self.hp = max(attacks.iteritems(), key=operator.itemgetter(1))
    def get_explanation(self):
        return "{:.1f} HP in one attack".format(self.hp)
        
class weakling(achievement):
    def __init__(self, dmgDict):
        super(weakling, self).__init__(dmgDict)
        self.title = "The Weakling"
        # Min HP in one attack
        attacks = {key: value["maxAttack"] for key, value in dmgDict.iteritems()}
        self.player, self.hp = min(attacks.iteritems(), key=operator.itemgetter(1))
    def get_explanation(self):
        return "{:.1f} HP in one attack".format(self.hp)
        
class useless(achievement):
    def __init__(self, dmgDict):
        super(useless, self).__init__(dmgDict)
        self.title = "Useless"
        # Min damage dealt
        attacks = {key: value["damageGiven"] for key, value in dmgDict.iteritems()}
        self.player, self.hp = min(attacks.iteritems(), key=operator.itemgetter(1))
    def get_explanation(self):
        return "{:.1f} HP total attack".format(self.hp)
        
class friendly_fire(achievement):
    def __init__(self, dmgDict):
        super(friendly_fire, self).__init__(dmgDict)
        self.title = "Friendly Fire"
        # Max single damage dealt to group
        FUs = {key: value["maxFU"] for key, value in dmgDict.iteritems()}
        self.player, self.hp = max(FUs.iteritems(), key=operator.itemgetter(1))
    def get_explanation(self):
        return "{:.1f} HP taken from group in one day".format(self.hp)
        
class liability(achievement):
    def __init__(self, dmgDict):
        super(liability, self).__init__(dmgDict)
        self.title = "Liability"
        # Max total damage dealt to group
        FUs = {key: value["damageTaken"] for key, value in dmgDict.iteritems()}
        self.player, self.hp = max(FUs.iteritems(), key=operator.itemgetter(1))
    def get_explanation(self):
        return "{:.1f} HP total taken from group".format(self.hp)
        
class safe_bet(achievement):
    def __init__(self, dmgDict):
        super(safe_bet, self).__init__(dmgDict)
        self.title = "Safe Bet"
        # Min total damage dealt to group
        FUs = {key: value["damageTaken"] for key, value in dmgDict.iteritems()}
        self.player, self.hp = min(FUs.iteritems(), key=operator.itemgetter(1))
    def get_explanation(self):
        return "only {:.1f} HP total taken from group".format(self.hp)

def get_achievement_dict(dmgDict):
    achmts = [best_player(dmgDict),\
        bravery(dmgDict),\
        coward(dmgDict),\
        damp_squib(dmgDict),\
        warrior(dmgDict),\
        weakling(dmgDict),\
        useless(dmgDict),\
        friendly_fire(dmgDict),\
        liability(dmgDict),\
        safe_bet(dmgDict)]
    achmt_dict = {}
    for achmt in achmts:
        achmt_dict[achmt] = achmt.get_weight()
    return achmt_dict
