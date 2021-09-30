from conexion import Conexion
from logger_base import log

class CursorDelPool:

    def __init__(self) -> None:
        self._conexion = None
        self._cursor = None

    def __enter__(self):
        log.debug('Start met with __enter__')
        self._conexion = Conexion.getConection()
        self._cursor = self._conexion.cursor()
        return self._cursor

    def __exit__(self, type_exception, value_exception, traceback_detail):
        log.debug(f'Method __exit__ executed')
        if value_exception:
            self._conexion.rollback()
            log.debug(f'Throw exception, rollback transaction: {value_exception}, {type_exception}, {traceback_detail}')
        else:
            self._conexion.commit()
            log.debug('Commit transaction')
        self._cursor.close()
        Conexion.looseConnection(self._conexion)


if __name__ == '__main__':
    with CursorDelPool() as cursor:
        log.debug('Inside block with')
        cursor.execute('SELECT * FROM test.personas')
        log.debug(cursor.fetchall())