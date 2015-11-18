#!/usr/bin/env python

# Read incoming party info in JSON format and output names, stats and battle info.

import json
import sys
import printing
import battle

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

# Print names, health and XP of party members.
print printing.title("Party Status", 1)

party_table = printing.table(["Name", "Level", "HP/Max HP", "XP/Max XP"])
for member in members:
    name = member["profile"]["name"]
    lvl = member["stats"]["lvl"]
    exp = member["stats"]["exp"]
    max_exp = round((0.25*lvl**2 + 10*lvl + 139.75)/10)*10
    hp = member["stats"]["hp"]
    party_table.add_row([name, lvl,
        str(int(round(hp))).rjust(2) + '/' + str(max_health) + ' ' +
            printing.progress_bar(hp, max_health, health_bar_width),
        str(int(round(exp))).rjust(4) + '/' + str(int(max_exp)).ljust(4) + ' ' +
            printing.progress_bar(exp, max_exp, exp_bar_width)])
print party_table


if "quest" in party_info and party_info["quest"]:
    # Print current boss and its health.
    print printing.title("Boss Status", 2)
    quest_key = party_info["quest"]["key"]
    quest = habitica_content["quests"][quest_key]
    if "boss" in quest:
        boss_hp = party_info["quest"]["progress"]["hp"]
        boss_max_hp = quest["boss"]["hp"]
        boss_name = quest["boss"]["name"]
        print 'Boss: {}'.format(boss_name)
        sys.stdout.write('{}/{} '.format(int(round(boss_hp)), boss_max_hp))
        sys.stdout.write(printing.progress_bar(boss_hp, boss_max_hp, boss_health_bar_width))
        sys.stdout.write('\n\n')
        print battle.summary(messages, boss_name)
