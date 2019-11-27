# coding:utf-8

import mysql.connector

my_db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="123123"
)

my_cursor = my_db.cursor()

# my_cursor.execute("CREATE DATABASE runoob_db")   # 创建数据库 runoob.db,只能创建一次

my_cursor.execute("SHOW DATABASES")  # 显示。。

for x in my_cursor:
    print(x)

