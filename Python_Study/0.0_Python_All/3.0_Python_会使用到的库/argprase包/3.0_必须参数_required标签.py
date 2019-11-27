# coding:utf-8


import argparse

parse = argparse.ArgumentParser(description="your script description")

# parse.add_argument("--verbose", help="verbose mode")

# required标签就是说 --verbose参数是必须的，并且类型是int型，输入别的类型会出错
parse.add_argument("--verbose", '-v', required=True, type=int)

# 将变量以 标签-值 的字典形式存入args字典
args = parse.parse_args()

if args.verbose:
    print("Verbose mode on!")
else:
    print("Verbose mode off!")


"""
=================运行======python 3.0_必须参数_required标签.py --verbose 2
Verbose mode on!

=================运行======python 3.0_必须参数_required标签.py -v 2
Verbose mode on!

"""




