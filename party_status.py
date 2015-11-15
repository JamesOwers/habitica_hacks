#!/usr/bin/env python

# Read incoming party info in JSON format and output names, stats and battle info.

import json
import sys

# Config ---------------------------------------------------#
max_health = 50             # Maximum player health
health_bar_width = 10       # Width of player health bars
exp_bar_width = 10          # Width of player exp bars
boss_health_bar_width = 20  # Width of boss' health bar
#-----------------------------------------------------------#

content_json = sys.stdin.readline()
party_json = sys.stdin.readline()
habitica_content = json.loads(content_json)
party_info = json.loads(party_json)

messages = party_info["chat"]
members = party_info["members"]


# Draw a progress bar
def progress_bar(value, max_value, width):
    sys.stdout.write('[')
    for i in range(int(round(width*value/max_value))):
        sys.stdout.write('#')
    for i in range(int(round(width*(max_value-value)/max_value))):
        sys.stdout.write('-')
    sys.stdout.write(']')


title = "Party Status"
sys.stdout.write('{}\n{}\n\n'.format(title, len(title)*"="))
topline = [
    "Name".ljust(15) + '\t',
    "hp/max",
    " "*(health_bar_width+2) + '\t',
    "exp".rjust(4) + '/' + "max".ljust(4) + " ",
    " "*(exp_bar_width+2)
]
tlstr = "".join(topline)
sys.stdout.write(tlstr + '\n')
sys.stdout.write("-"*len(tlstr.expandtabs(8)) + '  \n')

# Print names and health
for member in members:
    name = member["profile"]["name"]
    lvl = member["stats"]["lvl"]
    exp = member["stats"]["exp"]
    max_exp = 0.25*lvl**2 + 10*lvl + 139.75
    hp = member["stats"]["hp"]
    sys.stdout.write('{}\t{}/{} '.format(
            name.ljust(15),
            int(round(hp)),
            max_health
        )
    )
    progress_bar(hp, max_health, health_bar_width)
    sys.stdout.write('\t{}/{} '.format(
            str(int(round(exp))).rjust(4),
            str(int(round(max_exp))).ljust(4)
        )
    )
    progress_bar(exp, max_exp, exp_bar_width)
    sys.stdout.write('  \n')

# Print current boss and its health
if "quest" in party_info and "key" in party_info["quest"]:
    quest_key = party_info["quest"]["key"]
    quest = habitica_content["quests"][quest_key]
    if "boss" in quest:
        boss_hp = party_info["quest"]["progress"]["hp"]
        boss_max_hp = quest["boss"]["hp"]
        boss_name = quest["boss"]["name"]
        print '\nBoss: {}'.format(boss_name)
        sys.stdout.write('{}/{} '.format(int(round(boss_hp)), boss_max_hp))
        progress_bar(boss_hp, boss_max_hp, boss_health_bar_width)
        sys.stdout.write('\n')
