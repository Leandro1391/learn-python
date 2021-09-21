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
    # Los cambios nose van a autoguardar solamente lo usamos para relizar pruebas - the best approach is using keyboard
    #  with o realizar el commit manualmente con conn.commit()
    # conn.autocommit = False
    cursor = conn.cursor()

    sentence = 'INSERT INTO test.personas(nombre, apellido, email) VALUES(%s, %s, %s)'
    values = ('Leticia', 'America', 'lamerica@gmail.com')
    cursor.execute(sentence, values)

    sentence = 'UPDATE test.personas SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
    values = ('Fernando', 'Perez', 'fperez@gmail.com', 8)
    cursor.execute(sentence, values)

    conn.commit()
    print('Transaction End, commit done')
except Exception as e:
    conn.rollback()
    print(f'Exception - Rollback transaction: {e}, {type(e)}')
finally:
    conn.close()