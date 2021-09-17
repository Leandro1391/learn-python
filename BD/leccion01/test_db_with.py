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
            # sentence = 'SELECT id_persona, nombre FROM test.personas WHERE id_persona = %s'
            sentence = 'SELECT * FROM test.personas WHERE id_persona IN %s'
            # prymaries_keys = ((1,2,3),)
            enter = input('Proporciona los id\'s a buscar (separado por comas): ')
            prymaries_keys = (tuple(enter.split(',')),)
            # id_persona = input('Ingresar el valor de id_persona: ')
            cursor.execute(sentence, prymaries_keys)
            registros = cursor.fetchall()

            # Solamente trae un registro fetchone()
            # registro = cursor.fetchone()
            for registro in registros:
                print(registros)
except Exception as e:
    print(f'Exception - Error handled: {e}, {type(e)}')
finally:
    conn.close()