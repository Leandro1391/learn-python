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
    with conn.cursor() as cursor:
        sentence = 'INSERT INTO test.personas(nombre, apellido, email) VALUES(%s, %s, %s)'
        values = ('Alex', 'Ubago', 'aubago@gmail.com')
        cursor.execute(sentence, values)

        sentence = 'UPDATE test.personas SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
        values = ('Fernando', 'Perez', 'fperez@gmail.com', 8)
        cursor.execute(sentence, values)

except Exception as e:
    print(f'Exception - Rollback transaction: {e}, {type(e)}')
finally:
    conn.close()
    print('Transaction End, commit done')