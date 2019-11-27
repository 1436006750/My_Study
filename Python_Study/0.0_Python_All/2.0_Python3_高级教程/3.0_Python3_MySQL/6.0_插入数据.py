# coding:utf-8

import mysql.connector

my_db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="123123",
    database="runoob_db"
)

my_cursor = my_db.cursor()

sql = "insert into sites(name, url) VALUES (%s, %s)"
val = ("RUNOOB", "http://ww.runoob.com")

my_cursor.execute(sql, val)

my_db.commit()    # 数据表内容有更新，必须要使用的语句

print(my_cursor.rowcount, "记录插入成功!")







