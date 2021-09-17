import psycopg2

# 1) Create conection object
conn = psycopg2.connect(
    user='leandro', 
    password='',
    host='localhost',
    port='5432',
    database='postgres'
)



try:
    with conn:
        with conn.cursor() as cursor:
            sentence = 'SELECT * FROM test.personas'
            cursor.execute(sentence)
            registros = cursor.fetchall()
            print(registros)
except Exception as e:
    print(f'Exception - Error handled: {e}, {type(e)}')
finally:
    conn.close()