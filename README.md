# habitica_hacks
Scripts for habitica based fun

## Scripts

### battle_summary.py

To use:

1. Go to Habitica [Social > Party](img/party.png), and copy the contents of the [party chat](img/party_chat.png) into a text file. I've called mine [`habitica_battle.txt`](img/habitica_battle.png) and put it in the Downloads folder; if you choose somewhere different, replace `~/Downloads/habitica_battle.txt` in the usage below
1. Download the python file `battle_summary.py`
1. open your terminal, navigate to where you downloaded it, and run the example usage

Example usage:
    $ cat ~/Downloads/habitica_battle.txt | python battle_summary.py

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
```
Sploshy attacks Vice's Shade for 5.6 damage, Vice's Shade attacks party for 3.1 damage. -2 days ago+1   
Jozef Mokry attacks Vice's Shade for 3.8 damage, Vice's Shade attacks party for 0.0 damage. -2 days ago+1   
kungfujam casts Valorous Presence for the party. -2 days ago+1   
Nyne attacks Vice's Shade for 18.6 damage, Vice's Shade attacks party for 1.5 damage. -2 days ago+1   
Deena Bardsley attacks Vice's Shade for 24.0 damage, Vice's Shade attacks party for 1.5 damage. -2 days ago+1   
onemorego attacks Vice's Shade for 79.8 damage, Vice's Shade attacks party for 1.3 damage. -2 days ago+1   
Sploshy attacks Vice's Shade for 7.2 damage, Vice's Shade attacks party for 2.8 damage. -3 days ago+1   
kungfujam casts Valorous Presence for the party. -3 days ago+1   
Deena Bardsley attacks Vice's Shade for 14.5 damage, Vice's Shade attacks party for 0.0 damage. -3 days ago+1   
kungfujam casts Valorous Presence for the party. -3 days ago+1   
kungfujam attacks Vice's Shade for 28.4 damage, Vice's Shade attacks party for 1.1 damage. -3 days ago+1   
onemorego attacks Vice's Shade for 13.5 damage, Vice's Shade attacks party for 0.0 damage. -3 days ago+1   
Sploshy attacks Vice's Shade for 8.5 damage, Vice's Shade attacks party for 0.0 damage. -4 days ago+1   
Jozef Mokry attacks Vice's Shade for 1.1 damage, Vice's Shade attacks party for 3.0 damage. -4 days ago+1   
s0min attacks Vice's Shade for 2.3 damage, Vice's Shade attacks party for 0.0 damage. -4 days ago+1   
cool ting: just found you can look at your point history in a nice graph by clicking the histogram item on the RHS of the yellow bar at the top. Fun! You can see if you've had any dips! -4 days ago+1         
 kungfujam 
I really don't get attack times...@s0min Matt, do you have a really weird day refresh time? -4 days ago+1         
 kungfujam 
They're cool. -4 days ago+1         
 Nyne 
Sploshy and Lemonzakura are my friends Michael and James. -4 days ago+1         
 Nyne 
s0min attacks Vice's Shade for 9.6 damage, Vice's Shade attacks party for 0.0 damage. -4 days ago+1   
kungfujam casts Intimidating Gaze for the party. -4 days ago+1   
kungfujam casts Intimidating Gaze for the party. -4 days ago+1   
kungfujam casts Valorous Presence for the party. -4 days ago+1   
kungfujam casts Valorous Presence for the party. -4 days ago+1   
kungfujam casts Valorous Presence for the party. -4 days ago+1   
kungfujam casts Valorous Presence for the party. -4 days ago+1   
```
