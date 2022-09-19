import pymysql

# connecting with sql
conn = pymysql.connect(user='root', password='welcome$1234', host='127.0.0.1', database="sqltable")
mycursor = conn.cursor()

# creating table
sql_query = '''create table if not exists pysalarydata
(
id int,
namess text,
age int,
address text,
salary dec
)
'''
mycursor.execute(sql_query)

# inserting data
mycursor.execute('''
insert into pysalarydata values
( 
1, "ramesh",32, "ahmedabad",2000.0
);
''')

mycursor.execute('''
insert into pysalarydata values
( 
2, "abhishek", 24, "Belgaum", 100000.0

)
''')
mycursor.execute('SHOW TABLES')

# printing data
mycursor.execute("SELECT * FROM sqltable.pysalarydata;")

while True:
    row = mycursor.fetchone()
    if row is not None:
        print(row)
    else:
        break

for table in mycursor:
    print(table[0])
mycursor.close()
conn.close()
