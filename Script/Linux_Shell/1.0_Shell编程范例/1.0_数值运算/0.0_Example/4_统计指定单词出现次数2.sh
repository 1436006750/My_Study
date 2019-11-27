#!/bin/bash

if [ $# -lt 1 ]; then
    echo "ERROR: you should input 2 words at least";
    echo "Usage: basename $0 FILE WORDS ...."
    exit -1
fi

FILE=$1
((WORDS_NUM=$#-1))

for n in $(seq $WORDS_NUM)
do
    shift
    cat $FILE | sed -e "s/[^a-zA-Z]/\n/g" \
        | grep -v ^$ | sort | uniq -c | grep " $1$"
done


