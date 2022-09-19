import pymysql

conn = pymysql.connect(user='root', password='welcome$1234', host='127.0.0.1', database="TEST_PYTHON_SQL")
cursor = conn.cursor()
cursor.execute("update players set name ='hitman' where name='sachin' ")
conn.commit()

cursor.close()
conn.close()