#!/usr/bin/bash

# basically the same as codegrep, but for find command

script_name=`basename $0`

if [[ -z $1 ]]; then
    echo "Invalid usage of ${script_name}. Exemplary usage: ${script_name} script.py"
    exit 1
fi

find . -name "$1"
