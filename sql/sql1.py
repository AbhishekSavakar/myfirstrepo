import pymysql
conn = pymysql.connect(user='root',password='welcome$1234',host='127.0.0.1')
cursor=conn.cursor()
cursor.execute("CREATE DATABASE TEST_PYTHON_SQL")

cursor.close()
conn.close()