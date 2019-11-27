# coding:utf-8

import mysql.connector

my_db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="123123",
  database="runoob_db"
)
my_cursor = my_db.cursor()

my_cursor.execute("select * from sites")

my_result = my_cursor.fetchall()    # fetchall() 获取所有的记录

for x in my_result:
    print(x)







