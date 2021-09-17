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
            sentence = 'UPDATE test.personas SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
            values = (
                ('Julio', 'Fernandez', 'jfernandez@gmail.com', 3),
                ('Pepe', 'Argento', 'pargento@gmail.com', 5)
            )
            cursor.executemany(sentence, values)
            registros_actualizados = cursor.rowcount
            print(f'Registros actualizados: {registros_actualizados}')
            
except Exception as e:
    print(f'Exception - Error handled: {e}, {type(e)}')
finally:
    conn.close()