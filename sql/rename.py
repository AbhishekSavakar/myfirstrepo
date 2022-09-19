import pymysql

conn = pymysql.connect(user='root', password='welcome$1234', host='127.0.0.1', database="TEST_PYTHON_SQL")
cursor = conn.cursor()
cursor.execute("alter table players rename column role to speciality ")
conn.commit()

cursor.close()
conn.close()