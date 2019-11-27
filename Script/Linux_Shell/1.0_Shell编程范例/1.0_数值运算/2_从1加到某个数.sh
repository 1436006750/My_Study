#!/bin/bash

read -p "please input a num: " num
sum=0
for i in $(seq $num)
do
sum=$((sum+i))
done
echo "result is $sum"
