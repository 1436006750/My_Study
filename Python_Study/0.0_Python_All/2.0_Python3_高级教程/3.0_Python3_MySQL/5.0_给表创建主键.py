# coding:utf-8

import mysql.connector

my_db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="123123",
    database="runoob_db"
)

my_cursor = my_db.cursor()

my_cursor.execute("create table sites(id int AUTO_INCREMENT PRIMARY KEY, "
                  "name VARCHAR(255), url VARCHAR(255))")








