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
            sentence = 'DELETE FROM test.personas WHERE id_persona IN %s'
            enter = input('Ingresar el id_persona a eliminar (separados por comas): ')
            values = (tuple(enter.split(',')),)
            cursor.execute(sentence, values)
            registros_eliminados = cursor.rowcount
            print(f'Registros eliminados: {registros_eliminados}')
            
except Exception as e:
    print(f'Exception - Error handled: {e}, {type(e)}')
finally:
    conn.close()