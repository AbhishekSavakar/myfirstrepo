import pymysql

def insert_rows(name,country,team):
    conn = pymysql.connect(user='root',password='welcome$1234',host='127.0.0.1',database="TEST_PYTHON_SQL")
    cursor=conn.cursor()
    sql_query = f"insert into players(Name,Country,IPL_team) values ('{name}','{country}','{team}')"
    print(sql_query)

    try:
        cursor.execute(sql_query)
        conn.commit()
        print("1 row inserted")
    except Exception as ex:
        print('Error')
        message = f'''An exception of type {type(ex).__name__} occurred. Arguments:{ex.args}'''
        print(message)
        conn.rollback()

    finally:
        cursor.close()
        conn.close()

n = int(input('how many rows : '))
for i in range(n):
    name = input('Enter name : ')
    country = input('Enter country : ')
    team = input('Enter IPL team : ')
    insert_rows(name, country, team)

    print('-------------------------------------')




