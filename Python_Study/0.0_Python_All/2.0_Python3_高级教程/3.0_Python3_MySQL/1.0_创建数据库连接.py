# coding:utf-8

import mysql.connector

my_db = mysql.connector.connect(
    host="localhost",      # 数据库主机地址
    user="test",   # 数据库用户名
    passwd="123123"  # 数据库密码
)

print(my_db)


"""
ConnectionRefusedError: [Errno 111] Connection refused
"""






