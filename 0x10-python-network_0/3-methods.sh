#!/bin/bash
#options
curl -I -s $1 | grep "Allow:" | sed 's/Allow://i'
