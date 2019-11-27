#!/bin/expect

# 使用命令：expect login_L4.sh 172.16.68.41

set timeout 4
set ip [lindex $argv 0]
spawn ssh root@$ip

expect {
         "yes/no" {send "yes\r"; exp_continue}
         "password" {send "passw0rd\r"}
}

interact
