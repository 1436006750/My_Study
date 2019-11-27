# coding:utf-8

import sys


def fi_bo_na_qi(n):    # 生成器函数----斐波那契
    a, b, counter = 0, 1, 0

    while True:
        if counter > n:
            return
        yield a
        a, b = b, a + b
        counter += 1


f = fi_bo_na_qi(10)    # f 是一个迭代器，由生成器返回生成

while True:
    try:
        print(next(f), end=" ")
    except StopIteration:
        sys.exit()


# 输出结果：0 1 1 2 3 5 8 13 21 34 55

