#!/usr/bin/python

import pexpect


def ssh_connnect():
    print('1')
    process = pexpect.spawn('ssh root@172.16.68.41')
    print(process)
    if process.expect('password', timeout=30, searchwindowsize=20):
        process.send('passw0rd\n')
    print '3'
    process.interact()
    print '4'


def main_function():
    print('Start.....')
    ssh_connnect()


if __name__ == '__main__':
    main_function()
