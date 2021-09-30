from typing import List
from persona import Persona
from conexion import Conexion
from logger_base import log

# DAO: Data Access Object: es el patrón de diseño para comunicarse una una BD
# CRUD: Create Read Update Delete

class PersonaDao(Persona, Conexion):

    _SELECCIONAR = 'SELECT * FROM test.personas ORDER BY id_persona'
    _INSERTAR = 'INSERT INTO test.personas(nombre, apellido, email) VALUES(%s, %s, %s)'
    _ACTUALIZAR = 'UPDATE test.personas SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
    _ELIMINAR = 'DELETE FROM test.personas WHERE id_persona=%s'

    def __init__(self, nombre, apellido, email):
        super().__init__(nombre, apellido, email)        

    @classmethod
    def seleccionar(cls):
        with Conexion.getCursor() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            listPersonas: List[Persona] = []
            for registro in registros:
                persona = Persona(registro[0], registro[1], registro[2], registro[3])
                listPersonas.append(persona)
            return listPersonas

    @classmethod
    def insertar(cls, persona: Persona):
        with Conexion.getConection():
            with Conexion.getCursor() as cursor:
                values = (persona.nombre, persona.apellido, persona.email)
                cursor.execute(cls._INSERTAR, values)
                log.debug(f'person inserted: {persona}')
                return cursor.rowcount

    @classmethod
    def actualizar(cls, persona: Persona):
        with Conexion.getConection():
            with Conexion.getCursor() as cursor:
                values = (persona.nombre, persona.apellido, persona.email, persona.id_persona)
                cursor.execute(cls._ACTUALIZAR, values)
                log.debug(f'person inserted: {persona}')
                return cursor.rowcount

    @classmethod
    def eliminar(cls, persona: Persona):
        with Conexion.getConection():
            with Conexion.getCursor() as cursor:
                values = (persona.id_persona,)
                cursor.execute(cls._ELIMINAR, values)
                log.debug(f'person deleted: {persona}')
                return cursor.rowcount

                


if __name__ == '__main__':

    # Eliminar un registro
    personaOne = Persona(id=16)
    persons_deleted = PersonaDao.eliminar(personaOne)
    log.debug(f'Person deleted: {persons_deleted}')


    #Actualizar un registro
    personaOne = Persona(nombre='Floro', apellido='Nerone', email='fnerone@gmail.com', id=15)
    persons_updated = PersonaDao.actualizar(personaOne)
    log.debug(f'Person inserted: {persons_updated}')

    #Insertar un registro
    # personOne = Persona(nombre='Josephine', apellido='Clark', email='jclark@gmail.com')
    # persons_inserted = PersonaDao.insertar(personOne)
    # log.debug(f'Person inserted: {persons_inserted}')

    # Selecionar objectos
    personas = PersonaDao.seleccionar()
    for persona in personas:
        log.debug(persona)