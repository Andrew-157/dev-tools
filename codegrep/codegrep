#!/usr/bin/bash

# basically a wrapper for grep(so I don't need to enter most used options manually all the time), but in the future maybe I will re-write it in C and make it fancy for myself

# TODO: allow to specify dir
# TODO: nocolor option

script_name=`basename $0`

if [[ -z $1 ]]; then
    echo "Invalid usage of ${script_name}. Exemplary usage: ${script_name} \"void func\""
    exit 1
fi

HELP_TEXT=$(cat << EOF
${script_name} - Search for stuff without a need to type all grep options\nOptions:\n
\t-h, --help - print this message and exit\n
\t--noci - disable case-insensitive search
EOF
)

if [[ $1 == "--noci" ]]; then
    # noci - No-Case-Insensitive
    # TODO: need to add here a check that search pattern was provided
    grep "$2" --color=always -R ./ -I --exclude-dir=.git/
elif [[ $1 == "-h" ]] || [[ $1 == "--help" ]]; then
    echo -e $HELP_TEXT
    exit 0
elif [[ -n $2 ]]; then
    echo "Invalid usage of ${script_name}. More than one positional arguments are not allowed, use quotes for a search pattern."
    exit 1
else
    grep "$1" --color=always -R ./ -Ii --exclude-dir=.git/
fi
