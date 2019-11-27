# coding:utf-8
import argparse

parse = argparse.ArgumentParser(description="your script description")
# description参数可以用于插入描述脚本用途的信息，可以为空

# 添加--verbose标签，标签别名可以为-v，这里action的意思是当读取的参数中出现--verbose/-v的时候
# 参数字典的verbose建对应的值为True，而help参数用于描述--verbose参数的用途或意义。
parse.add_argument("--verbose", '-v', action="store_true", help="verbose mode")

# 将变量以 标签-值 的字典形式存入args字典
args = parse.parse_args()

if args.verbose:
    print("Verbose mode on!")
else:
    print("Verbose mode off!")


"""
运行python test.py后面跟了--verbose/-v的时候会输出前者，如果什么都没有会输出后者。
如果输入了--verbose/-v以外的参数则会报错：unrecognized arguments
稍微提一下，action参数表示值赋予键的方式，这里用到的是bool类型；
如果是'count'表示将--verbose标签出现的次数作为verbose的值；
'append'表示将每次出现的该便签后的值都存入同一个数组再赋值。（嘛，一般后面两种用的比较少就不多说了）
PS：--help标签在使用argparse模块时会自动创建，因此一般情况不需要我们主动定义帮助信息。
"""

"""
========================================== python 2.0_一般形式_test.py -v
Verbose mode on!

===============运行========================python 2.0_一般形式_test.py --help
usage: 2.0_一般形式_test.py [-h] [--verbose]

your script description

optional arguments:
  -h, --help     show this help message and exit
  --verbose, -v  verbose mode
"""