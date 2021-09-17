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
            sentence = 'INSERT INTO test.personas(nombre, apellido, email) VALUES(%s, %s, %s)'
            # se puede realizar de esta forma porque estoy enviando una tupla de tuplas en values
            values = (
                ('Esteban', 'Estevez', 'eestevez@gmail.com'),
                ('Rebeca', 'Garcia', 'rgarcia@gmail.com'),
                ('Maria', 'Rosa', 'mrosa@gmail.com')
            )
            # cursor.execute(sentence, values)
            cursor.executemany(sentence, values)
            # Tenemos que confirmar la transaccion pero como estamos usamos with no necesitamos confirmar en forma explicita
            # conn.commit()
            registros_insertados = cursor.rowcount
            print(f'Registros Insertados: {registros_insertados}')
            
except Exception as e:
    print(f'Exception - Error handled: {e}, {type(e)}')
finally:
    conn.close()