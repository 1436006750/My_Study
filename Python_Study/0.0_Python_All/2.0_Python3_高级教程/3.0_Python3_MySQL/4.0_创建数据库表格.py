# coding:utf-8

import mysql.connector

my_db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="123123",
    database="runoob_db"    # 直接连接
)

my_cursor = my_db.cursor()

# my_cursor.execute("CREATE TABLE sites(name VARCHAR(255), url VARCHAR(255))")


my_cursor.execute("SHOW TABLES")

for x in my_cursor:
    print(x)


