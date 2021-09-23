import psycopg2

class Conexion:

    DATABASE: str = 'postgres'
    USERNAME: str = 'leandro'
    PASSWORD: str = ''
    DB_PORT: str = '5432'
    HOST: str = 'localhost'
    
    conexion = psycopg2.connect(
        user = USERNAME,
        password = PASSWORD,
        host = HOST,
        port = DB_PORT,
        database = DATABASE
    )

    # cursor