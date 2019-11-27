#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:zx
# datetime:19-11-21 下午2:04
# software: PyCharm

import subprocess


# 执行Linux命令
def run_cmd(cmd):
    print('running cmd: %s' % cmd)
    # pdb.set_trace()
    try:
        pipes = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                                 stderr=subprocess.PIPE, shell=True)
        # 使用 Popen.communicate() 来等待外部程序执行结束
        # print(pipes)
        std_out, std_err = pipes.communicate()
        std_out = '\n' + std_out.strip().decode('utf-8') + \
                  '\n----------------------------------------------------'
        if std_err.strip().decode('utf-8') == '':
            std_err = 'Null'
        # std_err = '\n' + std_err.strip().decode('utf-8')
        std_err = std_err
        print('std_out: %s' % std_out)
        print('std_err: %s' % std_err)
        return pipes.returncode, std_out, std_err
    # 使用 a1, a2, a3 = 来接收这个 return
    # a1：0表示进程运行结束  a2：std_out    a3：std_err
    except Exception as e:
        print('error when run command: %s' % e.message)



