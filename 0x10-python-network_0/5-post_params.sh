#!/bin/bash
#send a post message using curl
curl -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" $1
