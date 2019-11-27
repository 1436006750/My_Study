#!/bin/bash

read -p "please input a num1: " num1
read -p "please input a num2: " num2

result=`expr $num1 % $num2`

echo "$num1 % $num2 = $result"


let i=5%2
echo $i

echo 5 % 2 |bc

((i=5%2))
echo $i
