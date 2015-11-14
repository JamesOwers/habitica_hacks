# habitica_hacks
Scripts for habitica based fun

## Scripts

### battle_summary.py

To use:

1. Go to Habitica [Social > Party](img/party.png), and copy the contents of the [party chat](img/party_chat.png) into a text file. I've called mine [`habitica_battle.txt`](img/habitica_battle.png) and put it in the Downloads folder; if you choose somewhere different, replace `~/Downloads/habitica_battle.txt` in the usage below
1. Download the python file `battle_summary.py`
1. Open your terminal, navigate to where you downloaded it, and run the example usage

Example usage:
```bash 
cat ~/Downloads/habitica_battle.txt | python battle_summary.py
```

Example outputs:
```
Battle Summary
==============

User               | Damage given | Damage taken | K/D Ratio
-------------------|--------------|--------------|----------
Nyne               | 40.2         | 4.2          | 9.6      
Deena Bardsley     | 40.3         | 8.2          | 4.9      
s0min              | 17.2         | 0.0          | 17.2     
Sploshy            | 28.6         | 7.4          | 3.9      
onemorego          | 127.0        | 2.6          | 48.8     
kungfujam          | 64.8         | 2.2          | 29.5     
Jozef Mokry        | 10.1         | 3.0          | 3.4      

Achievements
-------------
*Best player*:      onemorego (48.8 K/D Ratio)  
*Bravery*:          Sploshy (4 attacks)  
*Coward*:           kungfujam (only 2 attacks)  
*Damp squib*:       Jozef Mokry (3.4 K/D Ratio)  
*The Warrior*:      onemorego (79.8 HP in one attack)  
*The Weakling*:     Jozef Mokry (3.8 HP in one attack)  
*Useless*:          Jozef Mokry (10.1 HP total attack)  
*Friendly Fire*:    Deena Bardsley (-6.7 HP taken from group in one day)  
*Liability*:        Deena Bardsley (-8.2 HP total taken from group)  
*Safe bet*:         s0min (-0.0 only HP total taken from group)
```

Example input:  
[Input file](data/habitica_battle.txt)

