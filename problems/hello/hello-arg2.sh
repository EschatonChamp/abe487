#!/bin/bash

set -u

if [[ $# -lt 1 ]]; then
	printf "Usage: %s GREETING [NAME]\n" "$(basename "$0")"
	exit 1
fi


GREETING=${1:-Hello}
NAME=${2:-Stranger}

echo "$GREETING, $NAME!"



