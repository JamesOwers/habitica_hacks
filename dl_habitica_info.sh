#!/bin/bash

# Request party info from server using curl.

user_id=`cat user_id`
api_key=`cat api_key`

habitica_content=`curl -sX GET https://habitica.com:443/api/v2/content`
party_info=`curl -sX GET -H "x-api-key:$api_key" -H "x-api-user:$user_id" https://habitica.com/api/v2/groups/party`

#member_info=`echo $party_info | sed -E 's/"special":\{[^}]+\},//g' | sed -E 's/"challenges":\[\]//g' | sed -E 's/.+"members":\[([^]]+)\].+/\1/'`

#members=`echo $member_info | grep -Eo '"(name|hp)":[^,]+'`

echo $habitica_content
echo $party_info
