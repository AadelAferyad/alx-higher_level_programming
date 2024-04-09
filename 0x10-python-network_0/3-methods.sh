#!/bin/bash
#options
curl -i -s -X OPTIONS $i | grep "Allow:" | sed 'i/Allow://i'
