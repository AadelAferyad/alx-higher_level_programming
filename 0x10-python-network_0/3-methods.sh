#!/bin/bash
#options
curl -I -s $i | grep "Allow:" | sed 's/Allow://i'
