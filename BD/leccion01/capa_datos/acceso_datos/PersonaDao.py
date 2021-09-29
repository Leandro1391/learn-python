from Persona import Persona
from Conexion import Conexion

class PersonaDao(Persona, Conexion):

    SELECCIONAR = 'SELECT * FROM test.personas'
    INSERTAR = 'INSERT INTO test.personas(nombre, apellido, email) VALUES(%s, %s, %s) '
    ACTUALIZAR = 'UPDATE test.personas SET WHERE'
    ELIMINAR = 'DELETE test.personas WHERE id_persona=%s'

    def __init__(self, nombre, apellido, email):
        super().__init__(nombre, apellido, email)        

    @classmethod
    def seleccionar(cls):
        try:
            Conexion.getCursor().execute(cls.SELECCIONAR)
            print(Conexion.getCursor().fetchall())
        except Exception as e:
            print(f'Exception - Error handled: {e}, {type(e)}')
        finally:
            Conexion.closeConection()

    @classmethod
    def insertar(cls, self):
        print(f'************{Persona.nombre} {Persona.apellido} {Persona.email}')
        cursor = cls.getCursor()
        try:
            # Conexion.getConection()
            
            value = (Persona.nombre, Persona.apellido, Persona.email)
            cursor.execute(cls.INSERTAR, value)
            cursor.commit()
            registro_insertado = cursor.rowcount
            print(f'Registros Insertados: {registro_insertado}')
        except Exception as e:
            print(f'Exception - Error handled: {e}, {type(e)}')
            cursor.rollback()
        finally:
            Conexion.closeConection()

    def actualizar(cls):
        cls.ACTUALIZAR

    def eliminar(cls):
        cls.ELIMINAR


if __name__ == '__main__':

    unaPersona = PersonaDao('Esteban', 'Pinti', 'epinti@gmail.com')
    personaDos = PersonaDao('Enrique', 'Garcia', 'egarcia@gmail.com')
    print(f'{unaPersona} - {personaDos}')