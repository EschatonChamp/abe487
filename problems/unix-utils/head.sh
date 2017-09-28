#!/bin/bash

set -u

if [[ $# -lt 1 ]]; then
	printf "Usage: %s FILE [NUM]\n" "$(basename "$0")"
fi

FILE=$1
NUM=${2:-3}
if [[ -f $FILE ]]; then
x=0
while read -r LINE; do
let x++
		if [[ x -lt $NUM ]] || [[ x -eq $NUM ]]; then
		echo "$LINE"
		fi
done < "$FILE"
else
	echo "\"$1\" is not a file"
	exit 1
fi


