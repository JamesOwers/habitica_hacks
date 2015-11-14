#!/usr/bin/env python

# Read incoming party info in JSON format and output names, stats and battle info.

import json
import sys

party_json = sys.stdin.readline()

party_info = json.loads(party_json)

messages = party_info["chat"]
members = party_info["members"]

# Print names and health
for member in members:
	health = member["stats"]["hp"]
	sys.stdout.write('{}\t{}/50 '.format(member["profile"]["name"].ljust(15), int(round(health))))
	sys.stdout.write('[')
	for i in range(int(health/5)):
		sys.stdout.write('#')
	for i in range(int((50-health)/5)):
		sys.stdout.write(' ')
	sys.stdout.write(']\n')
