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
            sentence = 'SELECT id_persona, nombre FROM test.personas WHERE id_persona = %s'
            id_persona = input('Ingresar el valor de id_persona: ')
            cursor.execute(sentence, (id_persona,))
            # registros = cursor.fetchall()
            # Solamente trae un registro fetchone()
            registros = cursor.fetchone()
            print(registro)
except Exception as e:
    print(f'Exception - Error handled: {e}, {type(e)}')
finally:
    conn.close()