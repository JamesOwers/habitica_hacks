#!/bin/bash

# Request habitica info from server using curl.

user_id=`cat user_id`
api_key=`cat api_key`

if ! [ -e 'cache' ]; then
	`mkdir cache`
fi

if ! [ -e 'cache/habitica_content.json' ]; then
	`curl -sX GET https://habitica.com:443/api/v2/content > cache/habitica_content.json`
fi
habitica_content=`cat 'cache/habitica_content.json'`
party_info=`curl -sX GET -H "x-api-key:$api_key" -H "x-api-user:$user_id" https://habitica.com/api/v2/groups/party`

echo $habitica_content
echo $party_info
