#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:zx
# datetime:19-11-21 下午4:56
# software: PyCharm

import pexpect
import argparse
import base_function
import pdb


def arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--ip', help='connect to ip ')
    return parser.parse_args()


def mian_finction():
    ip = arg_parser().ip
    print('ip = %s' % ip)
    cmd1 = 'expect login_L4.sh %s' % ip
    # cmd = cmd1
    # cmd2 = 'ls -al'
    # pdb.set_trace()
    # base_function.run_cmd(cmd)


if __name__ == '__main__':
    mian_finction()
