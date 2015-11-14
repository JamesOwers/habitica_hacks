#!/usr/bin/env python
"""
Takes as input a copy and paste from the social chat and outputs a summary of the battle

Example usage:
    $ cat ./data/habitica_battle.txt | python battle_summary.py

Example outputs:
Battle Summary
==============

User               | Damage given | Damage taken | K/D Ratio
-------------------|--------------|--------------|----------
Sooty              | 38.5         | 1.5          | 25.7     
BodgerNBadger      | 4.9          | 3.0          | 1.6      
Sweep              | 102.4        | 2.6          | 39.4     
l00zr              | 11.9         | 0.0          | 11.9     
Mr Blobby          | 29.2         | 3.0          | 9.7      
TRekd              | 64.8         | 2.2          | 29.5     
OakieDoke          | 21.3         | 5.9          | 3.6      

Achievements
-------------
*Best player*:  	Sweep (39.4 K/D Ratio)  
*Bravery*:      	Sweep (3 attacks)  
*Coward*:       	Sooty (only 2 attacks)  
*Damp squib*:   	BodgerNBadger (1.6 K/D Ratio)  
*The Warrior*:  	Sweep (79.8 HP in one attack)  
*The Weakling*: 	BodgerNBadger (3.8 HP in one attack)  
*Useless*:      	BodgerNBadger (4.9 HP total attack)  
*Friendly Fire*:	OakieDoke (-3.1 HP taken from group in one day)  
*Liability*:    	OakieDoke (-5.9 HP total taken from group)  
*Safe bet*:     	l00zr (-0.0 only HP total taken from group) 
"""
import sys
import re
import operator

# Regex examples
# $name casts $spell for the party. $posneg$nrdays days ago$likes
# Deena Bardsley attacks Vice's Shade for 13.5 damage, Vice's Shade attacks
# party for 0.0 damage. -2 days

# attack = re.compile(r"""
# ^([a-zA-z ]+) attacks\s
# ([a-zA-z' ]+) for\s
# ([0-9\.]+) damage,\s
# [a-zA-z' ]+ attacks party for\s
# ([0-9\.]+) damage
# """, re.VERBOSE)
attack = re.compile("^([a-zA-z0-9 ]+) attacks ([a-zA-z' ]+) for ([0-9\.]+) "
                    "damage, [a-zA-z' ]+ attacks party for ([0-9\.]+) damage")

dmgDict = {}
for line in sys.stdin:
    if attack.match(line):
        userName, bossName, damageGiven, damageTaken = \
            attack.search(line).groups()
        if userName in dmgDict.keys():
            dmgDict[userName]['damageGiven'] += float(damageGiven)
            dmgDict[userName]['damageTaken'] += float(damageTaken)
            dg = dmgDict[userName]['damageGiven']
            dt = dmgDict[userName]['damageTaken']
            dmgDict[userName]['kd'] = \
                dg / max(dt, 1)
            dmgDict[userName]['nrAttacks'] += 1
        else:
            dmgDict[userName] = {
                'bossName': bossName,
                'damageGiven': float(damageGiven),
                'damageTaken': float(damageTaken),
                'kd': float(damageGiven)/max(float(damageTaken), 1),
                'maxAttack': float(damageGiven),
                'maxFU': float(damageTaken),
                'nrAttacks': 1
            }
        if float(damageGiven) > dmgDict[userName]['maxAttack']:
            dmgDict[userName]['maxAttack'] = float(damageGiven)
        if float(damageTaken) > dmgDict[userName]['maxFU']:
            dmgDict[userName]['maxFU'] = float(damageTaken)

maxAttacks = {key: value['maxAttack'] for key, value in dmgDict.iteritems()}
maxMaxAttack = max(maxAttacks.iteritems(), key=operator.itemgetter(1))
minMaxAttack = min(maxAttacks.iteritems(), key=operator.itemgetter(1))
attacks = {key: value['damageGiven'] for key, value in dmgDict.iteritems()}
minTotAttack = min(attacks.iteritems(), key=operator.itemgetter(1))
maxFUs = {key: value['maxFU'] for key, value in dmgDict.iteritems()}
maxMaxFU = max(maxFUs.iteritems(), key=operator.itemgetter(1))
FUs = {key: value['damageTaken'] for key, value in dmgDict.iteritems()}
minTotFU = min(FUs.iteritems(), key=operator.itemgetter(1))
maxTotFU = max(FUs.iteritems(), key=operator.itemgetter(1))
kds = maxFUs = {key: value['kd'] for key, value in dmgDict.iteritems()}
maxkd = max(kds.iteritems(), key=operator.itemgetter(1))
minkd = min(kds.iteritems(), key=operator.itemgetter(1))
nrAttacks = {key: value['nrAttacks'] for key, value in dmgDict.iteritems()}
minNrAttacks = min(nrAttacks.iteritems(), key=operator.itemgetter(1))
maxNrAttacks = max(nrAttacks.iteritems(), key=operator.itemgetter(1))

pad = 15
print "Battle Summary\n" + "="*14 + "\n"
print "User" + pad*" " + "| Damage given | Damage taken | K/D Ratio"
print (4 + pad) * "-" + "|--------------|--------------|----------"
for key, value in dmgDict.iteritems():
    print key.ljust(4 + pad) + "| " + str(value["damageGiven"]).ljust(13)\
        + "| " + "{:.1f}".format(value["damageTaken"]).ljust(13) + "| "\
        + "{:.1f}".format(value["kd"]).ljust(9)

print "\nAchievements\n" + "-" * 13
print "*Best player*:  \t" + "%s (%0.1f K/D Ratio)  " % maxkd
print "*Bravery*:      \t" + "%s (%d attacks)  " % maxNrAttacks
print "*Coward*:       \t" + "%s (only %d attacks)  " % minNrAttacks
print "*Damp squib*:   \t" + "%s (%0.1f K/D Ratio)  " % minkd
print "*The Warrior*:  \t" + "%s (%0.1f HP in one attack)  " % maxMaxAttack
print "*The Weakling*: \t" + "%s (%0.1f HP in one attack)  " % minMaxAttack
print "*Useless*:      \t" + "%s (%0.1f HP total attack)  " % minTotAttack
print "*Friendly Fire*:\t" + "%s (-%0.1f HP taken from group in one day)  "\
    % maxMaxFU
print "*Liability*:    \t" + "%s (-%0.1f HP total taken from group)  "\
    % maxTotFU
print "*Safe bet*:     \t" + "%s (-%0.1f only HP total taken from group)  "\
    % minTotFU
