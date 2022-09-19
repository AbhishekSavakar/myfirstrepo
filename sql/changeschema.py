import pymysql

conn = pymysql.connect(user='root', password='welcome$1234', host='127.0.0.1', database="TEST_PYTHON_SQL")
cursor = conn.cursor()
cursor.execute("describe players")

indexlist=cursor.fetchall()
for i in indexlist:
    print(i)

cursor.close()
conn.close()