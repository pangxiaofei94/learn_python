#!/usr/bin/python3

import pymysql

# 打开数据库连接
db = pymysql.connect("localhost", "root", "root", "test")

# 使用cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用execute 方法执行sql查询
# cursor.execute("SELECT VERSION()")

# 使用execute() 方法获取单条数据
# data = cursor.fetchone()
sql = "SELECT * FROM `users`"

try:
	cursor.execute(sql)
	db.commit()
except:
	db.rollback()

data = cursor.fetchone()

print(data)

print(data.name)

db.close()