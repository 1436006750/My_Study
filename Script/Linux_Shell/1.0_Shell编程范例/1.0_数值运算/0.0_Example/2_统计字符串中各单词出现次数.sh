#!/bin/bash

wget -c http://tinylab.org

# 统计每个单词出现的次数
cat index.html | sed -e "s/[^a-zA-Z]/\n/g" | grep -v ^$ | sort | uniq -c

# 统计出现频率最高的前10个单词
# wget -c http://tinylab.org
cat index.html | sed -e "s/[^a-zA-Z]/\n/g" | grep -v ^$ | sort | uniq -c | sort -n -k 1 -r | head -10


#说明：
#
#    cat index.html: 输出 index.html 文件里的内容
#    sed -e "s/[^a-zA-Z]/\n/g": 把非字母字符替换成空格，只保留字母字符
#    grep -v ^$: 去掉空行
#    sort: 排序
#    uniq -c：统计相同行的个数，即每个单词的个数
#    sort -n -k 1 -r：按照第一列 -k 1 的数字 -n 逆序 -r 排序
#    head -10：取出前十行
