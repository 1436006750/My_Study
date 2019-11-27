#!/bin/bash

read -p "please input a num: " num

sum=`expr $num + 1`
echo "$num + 1 = $sum"

sum=`expr $num - 1`
echo "$num - 1 = $sum"