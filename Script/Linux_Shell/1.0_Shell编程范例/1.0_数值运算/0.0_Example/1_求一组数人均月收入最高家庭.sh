#!/bin/bash


[ $# -lt 1 ] && echo "please input the income file" && exit -1
[ ! -f $1 ] && echo "$1 is not a file" && exit -1

income=$1
awk '{
    printf("%d %0.2f\n", $1, $3/$2);
}' $income | sort -k 2 -n -r



#    [ $# -lt 1 ]：要求至少输入一个参数，$# 是 Shell 中传入参数的个数
#    [ ! -f $1 ]：要求输入参数是一个文件，-f 的用法见 test 命令，help test
#    income=$1：把输入参数赋给 income 变量，再作为 awk 的参数，即需处理的文件
#    awk：用文件第三列除以第二列，求出月均收入，考虑到精确性，保留了两位精度
#    sort -k 2 -n -r：这里对结果的 awk 结果的第二列 -k 2，即月均收入进行排序，按照数字排序 -n，并按照递减的顺序排序 -r。


# 运行方式
# chmod +x 1_求一组数人均月收入最高家庭.sh
# ./1_求一组数人均月收入最高家庭.sh income.txt
