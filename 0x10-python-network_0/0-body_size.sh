#!/bin/bash
#size of the downloaded body in bytes
curl -s -o /dev/null -w "%{size_download}" $1;echo ""
