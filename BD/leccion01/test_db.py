import psycopg2

# 1) Create conection object
conn = psycopg2.connect(
    user='leandro', 
    password='',
    host='localhost',
    port='5432',
    database='postgres'
)

print(conn)

# Create cursor -> allow us to execute sql sentences

# 2) Create object cursor for sentences
cursor = conn.cursor()

sentence = 'SELECT * FROM test.personas'

# 3) Execute sentence SQL
cursor.execute(sentence)

# 4) request all register with own sentences execute
registros = cursor.fetchall()

print(registros)

# Close Cursor
cursor.close()

# Close conn
conn.close()