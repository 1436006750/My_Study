#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:zx
# datetime:19-11-20 下午7:33
# software: PyCharm

import subprocess
import pdb


def run_cmd(cmd):
    print('running cmd: %s' % cmd)
    # pdb.set_trace()
    try:
        pipes = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                                 stderr=subprocess.PIPE, shell=True)
        # 使用 Popen.communicate() 来等待外部程序执行结束
        print(pipes)
        std_out, std_err = pipes.communicate()
        std_out = '\n' + std_out.strip().decode('utf-8') + \
                  '\n----------------------------------------------------'
        std_err = '\n' + std_err.strip().decode('utf-8')
        print('std_out: %s' % std_out)
        print('std_err: %s' % std_err)
        return pipes.returncode, std_out, std_err
    except Exception as e:
        print('error when run command: %s' % e.message)


def main():
    cmd1 = 'ls -al|grep zx|awk \'{print $1}\'|head -1'
    run_cmd(cmd1)
    cmd2 = 'ls -al| tail -n +2 |awk \'{print $2}\'|head -1'
    run_cmd(cmd2)


if __name__ == '__main__':
    main()
