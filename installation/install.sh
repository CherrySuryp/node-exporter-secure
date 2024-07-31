#!/bin/bash

read -p "Enter the new API_BEARER_TOKEN: " new_token
sed -i '' "s/API_BEARER_TOKEN: \".*\"/API_BEARER_TOKEN: \"$new_token\"/" docker-compose.yml
echo "API_BEARER_TOKEN has been updated."