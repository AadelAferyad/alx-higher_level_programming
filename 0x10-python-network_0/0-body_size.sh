#!/usr/bin/bash
#size of the downloaded body in bytes
if [ $# -eq 1 ];then curl -s -o /dev/null -w "%{size_download}" $1;echo "";fi
