import pymysql
conn = pymysql.connect(user='root',password='welcome$1234',host='127.0.0.1',database="TEST_PYTHON_SQL")
mycursor=conn.cursor()

sql_query = '''CREATE TABLE IF NOT EXISTS  
               Players (id INT AUTO_INCREMENT PRIMARY KEY , 
                          Name VARCHAR(255), 
                          Country VARCHAR(255),
                          IPL_team VARCHAR(255))'''
mycursor.execute(sql_query)
mycursor.execute('SHOW TABLES')

for table in mycursor:
    print(table[0])
mycursor.close()
conn.close()