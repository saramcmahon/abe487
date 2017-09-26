#!/bin/bash

if [[ $#  -lt 1 ]]; then
    echo "Usage: cat-n.sh file" 
    exit 1
fi 

FILE=$1
if [[ ! -f $FILE ]]; then
    echo "\"$FILE\" is not a file"
    exit 1
fi

i=0
while read -r LINE; do 
    let i++
    echo "$i $LINE"
done < "$FILE"


