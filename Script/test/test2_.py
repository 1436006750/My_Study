#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:zx
# datetime:19-11-21 下午1:55
# software: PyCharm


import base_function


def main():
    cmd = 'ls -alt'
    a1, a2, a3 = base_function.run_cmd(cmd)
    print(a1)  # 0,表示 进程 运行结束
    print(a2)  # std_out
    print(a3)  # std_err


if __name__ == '__main__':
    main()
