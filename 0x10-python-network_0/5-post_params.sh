#!/bin/bash
#send a post message using curl
curl -s -d email=test@gmail.com -d subject="I will always be here for PLD" $1
