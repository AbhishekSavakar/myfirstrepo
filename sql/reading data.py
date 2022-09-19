import pymysql
print('########## PRINT THE TABLE CONTENT #########')
conn = pymysql.connect(user='root', password='welcome$1234', host='127.0.0.1', database="TEST_PYTHON_SQL")
cursor = conn.cursor()
cursor.execute("select * from players")

while True:
    row=cursor.fetchone()
    if row is not None:
        print(row)
    else:
        break
cursor.close()
conn.close()