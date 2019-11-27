#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:zx
# datetime:19-11-19 下午7:58
# software: PyCharm

import sys
import subprocess


def run_cmd(cmd):
    print('running cmd: %s' % cmd)
    cmd_get1 = subprocess.call(cmd, shell=True)
    cmd_get2 = subprocess.Popen(cmd, shell=True)
    return 0


if __name__ == '__main__':
    cmd = 'ls -lt'
    run_cmd(cmd)
    sys.exit(1)


