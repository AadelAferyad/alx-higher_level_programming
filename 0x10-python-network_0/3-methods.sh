#!/bin/bash
#options
curl -I -s $i | grep "Allow:" | cut -d " " -f 2-
