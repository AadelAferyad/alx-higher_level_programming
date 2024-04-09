#!/bin/bash
#options
curl -i -s -X OPTIONS $i | grep "Allow:" | sed 's/Allow://i'
