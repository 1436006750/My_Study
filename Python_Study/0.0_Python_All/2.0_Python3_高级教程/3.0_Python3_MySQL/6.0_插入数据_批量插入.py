# coding:utf-8

import mysql.connector

my_db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="123123",
  database="runoob_db"
)
my_cursor = my_db.cursor()

sql = "INSERT INTO sites (name, url) VALUES (%s, %s)"
val = [
  ('Google', 'https://www.google.com'),
  ('Github', 'https://www.github.com'),
  ('Taobao', 'https://www.taobao.com'),
  ('stackoverflow', 'https://www.stackoverflow.com/')
]

my_cursor.executemany(sql, val)

my_db.commit()    # 数据表内容有更新，必须使用到该语句

print(my_cursor.rowcount, "记录插入成功。")







