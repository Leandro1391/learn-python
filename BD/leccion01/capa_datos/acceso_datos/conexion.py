import sys
from logger_base import log
import psycopg2 as bd

class Conexion:

    _DATABASE = 'postgres'
    _USERNAME = 'leandro'
    _PASSWORD = ''
    _DB_PORT = '5432'
    _HOST = 'localhost'
    _conn = None
    _cursor = None
    

    @classmethod
    def getConection(cls):
        if cls._conn is None or cls._conn.closed:
            try:
                cls._conn = bd.connect(host=cls._HOST,
                    user=cls._USERNAME,
                    password=cls._PASSWORD,
                    port=cls._DB_PORT,
                    database=cls._DATABASE
                )
                log.debug(f'Conexion exitosa: {cls._conn}')
                return cls._conn
            except Exception as e:
                log.error(f'Exception - Error handled: {e}, {type(e)}')
                sys.exit()
        else:
            return cls._conn

    @classmethod
    def getCursor(cls):
        if cls._cursor is None or cls._cursor.closed:
            try:
                print('Estoy en el TRY del get Cursor')
                cls._cursor = cls.getConection().cursor()
                print(cls._cursor)
                log.debug(f'The cursor has been opened success: {cls._cursor}')
                return cls._cursor
            except Exception as e:
                log.error(f'Exception to get cursor- Error handled: {e}, {type(e)}')
                sys.exit()
        else:
            return cls._cursor


if __name__ == '__main__':
    Conexion.getConection()
    Conexion.getCursor()