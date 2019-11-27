# coding:utf-8


"""
表示该参数能接受的值只能来自某几个值候选值中，除此以外会报错，用choices参数即可。比如：
parser.add_argument('filename', choices=['test1.txt', 'text2.txt'])
"""


import argparse

parser = argparse.ArgumentParser(description="候选参数！！")

parser.add_argument('filename', choices=['text1.txt', 'text2.txt'])

args = parser.parse_args()

print("Read om %s" % (args.filename))


"""
 ============================python 7.0_候选参数_choices.py text2.txt
Read om text2.txt
============================ python 7.0_候选参数_choices.py text1.txt
Read om text1.txt
=============================python 7.0_候选参数_choices.py text.txt
usage: 7.0_候选参数_choices.py [-h] {text1.txt,text2.txt}
7.0_候选参数_choices.py: error: argument filename: invalid choice: 'text.txt' (choose from 'text1.txt', 'text2.txt')
"""


