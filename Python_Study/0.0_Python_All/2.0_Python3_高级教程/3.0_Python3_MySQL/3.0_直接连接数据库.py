# coding:utf-8

import mysql.connector

my_db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="123123",
    database="runoob_db"    # 直接连接
)

# 成功----存在这个数据库
# 失败----没有这个数据库

print(my_db)





