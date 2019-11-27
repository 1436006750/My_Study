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

my_result = my_cursor.fetchone()    # fetchone() 获取一条记录

print(my_result)








