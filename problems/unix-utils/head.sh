#!/bin/bash

if [[ $# -lt 1 ]]; then
printf "Usage: head.sh FILE [NUM]"
exit 1
fi

set -u

FILE=$1
NAME=${2:-3}

ls | head $FILE -n$NAME









