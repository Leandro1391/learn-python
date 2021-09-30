import sys
from logger_base import log
from psycopg2 import pool

class Conexion:

    _DATABASE = 'postgres'
    _USERNAME = 'leandro'
    _PASSWORD = ''
    _DB_PORT = '5432'
    _HOST = 'localhost'
    _MIN_CONN = 1
    _MAX_CONN = 5
    _pool = None
    
    @classmethod
    def getPool(cls):
        if cls._pool is None:
            try:
                cls._pool = pool.SimpleConnectionPool(cls._MIN_CONN, cls._MAX_CONN,
                                                            host = cls._HOST,
                                                            user = cls._USERNAME,
                                                            password = cls._PASSWORD,
                                                            port = cls._DB_PORT,
                                                            database = cls._DATABASE)
                log.debug(f'Success create pool {cls._pool}')
                return cls._pool
            except Exception as e:
                log.error(f'Exception to get pool: {e}, {type(e)}')
                sys.exit()
        else:
            return cls._pool

    @classmethod
    def getConection(cls):
        conexion = cls.getPool().getconn()
        log.debug(f'Conexion obtenido del pool: {conexion}')
        return conexion

    @classmethod
    def looseConnection(cls, conexion):
        cls.getPool().putconn(conexion)
        log.debug(f'We return the pool conection: {conexion}')

    @classmethod
    def closeConetions(cls):
        cls.getPool().closeall()

    @classmethod
    def getCursor(cls):
        pass

if __name__ == '__main__':
    conexion1 = Conexion.getConection()
    Conexion.looseConnection(conexion1)
    conexion2 = Conexion.getConection()
    conexion3 = Conexion.getConection()
    Conexion.looseConnection(conexion3)
    conexion4 = Conexion.getConection()
    conexion5 = Conexion.getConection()
    Conexion.looseConnection(conexion5)
    conexion6 = Conexion.getConection()