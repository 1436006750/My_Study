#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import pexpect


def ssh_cmd(user, ip, cmd, passwd):
    import pdb
    pdb.set_trace()
    ssh = pexpect.spawn('ssh %s@%s "%s"' % (user, ip, cmd))
    try:
        i = ssh.expect(['password:', 'continue connecting (yes/no)?'], timeout=-1)
        if i == 0:
            ssh.sendline(passwd)
        elif i == 1:
            ssh.sendline('yes')
            ssh.expect('password: ')
            ssh.sendline(passwd)
    except pexpect.EOF:
        print "EOF"
    except pexpect.TIMEOUT:
        print "TIMEOUT"

    ssh.interact()


if __name__ == '__main__':

    ssh_cmd('root', '172.16.68.41', 'ls -al', 'passw0rd')
