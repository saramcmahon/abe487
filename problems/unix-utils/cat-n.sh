#!/bin/bash

if [[ $#  -lt 1 ]]; then
printf "Usage: cat-n.sh file" 
exit 1

fi

cat -n $1

