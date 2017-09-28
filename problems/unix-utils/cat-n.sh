#!/bin/bash

if [[ $# -ne 1 ]]; then
    printf "Usage: %s FILE\n" "$(basename "$0")"
    exit 1
fi

FILE=$1
if [[ -f $FILE ]]; then
x=0
while read -r LINE; do
    let x++
    echo "$x $LINE"
done < $FILE
else 
	echo "\"$1\" is not a file"
	exit 1
fi
