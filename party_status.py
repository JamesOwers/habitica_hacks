# Print status of party: health, XP etc.

import sys
import printing
import quest

# Config ---------------------------------------------------#
max_health = 50             # Maximum player health
health_bar_width = 10       # Width of player health bars
exp_bar_width = 10          # Width of player exp bars
#-----------------------------------------------------------#

def print_status(party_info):
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
