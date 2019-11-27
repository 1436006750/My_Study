# coding:utf-8

import argparse
parser = argparse.ArgumentParser(description="your script description")

parser.add_argument('file', type=argparse.FileType('r'))    # 读取文件
args = parser.parse_args()
for line in args.file:
    print(line.strip())

"""
有问题
"""




