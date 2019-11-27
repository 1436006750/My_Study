# coding:utf-8

import argparse

"""
位置参数与sys.argv调用比较像，参数没有显式的--xxx或者-xxx标签，因此调用属性也与sys.argv相同
"""


parse = argparse.ArgumentParser(description="your script description")

parse.add_argument('filename')  # 输入的第一个参数 赋予 名为filename的键

# 将变量以 标签-值 的字典形式存入args字典
args = parse.parse_args()

print("Read om %s" % (args.filename))


"""
=========运行=======python 4.0_位置参数_positional_arguments.py test.txt
=========结果=======Read om test.txt
"""


"""
此外，可以用nargs参数来限定输入的位置参数的个数，默认为1。当然nargs参数也可用于普通带标签的参数。
parser.add_argument('num', nargs=2, type=int)表示脚本可以读入两个整数赋予num键（此时的值为2个整数的数组）。
nargs还可以'*'用来表示如果有该位置参数输入的话，之后所有的输入都将作为该位置参数的值；
‘+’表示读取至少1个该位置参数。
'?'表示该位置参数要么没有，要么就只要一个。
（PS：跟正则表达式的符号用途一致。）比如用：

parser.add_argument('filename')
parser.add_argument('num', nargs='*)

就可以运行python test.py text.txt 1 2
由于没有标签，所以用位置参数的时候需要比较小心。
"""