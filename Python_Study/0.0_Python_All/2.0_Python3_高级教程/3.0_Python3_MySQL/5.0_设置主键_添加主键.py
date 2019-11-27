# coding:utf-8

import mysql.connector

my_db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="123123",
    database="runoob_db"
)

my_cursor = my_db.cursor()

my_cursor.execute("ALTER TABLE sites ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")






