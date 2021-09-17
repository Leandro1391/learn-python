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
            values = ('Charles', 'Lennon', 'clennon@gmail.com')
            cursor.execute(sentence, values)
            # Tenemos que confirmar la transaccion pero como estamos usamos with no necesitamos confirmar en forma explicita
            # conn.commit()
            registros_insertados = cursor.rowcount
            print(f'Registros Insertados: {registros_insertados}')
            
except Exception as e:
    print(f'Exception - Error handled: {e}, {type(e)}')
finally:
    conn.close()