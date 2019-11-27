# coding:utf-8

import argparse

"""
位置参数与sys.argv调用比较像，参数没有显式的--xxx或者-xxx标签，因此调用属性也与sys.argv相同
"""


parse = argparse.ArgumentParser(description="your script description")

parse.add_argument('filename', default='text.txt')  # 输入的第一个参数 赋予 名为filename的键

# 将变量以 标签-值 的字典形式存入args字典
args = parse.parse_args()

print("Read om %s" % (args.filename))






"""
====================================python 6.0_默认参数值.py
usage: 6.0_默认参数值.py [-h] filename
6.0_默认参数值.py: error: the following arguments are required: filename
"""
