from logger_base import log


class Persona:

    def __init__(self, id=None, nombre=None, apellido=None, email=None):
        self._id_persona = id
        self._nombre = nombre
        self._apellido = apellido
        self._email = email

    @property
    def id_persona(self):
        return self._id_persona

    # @id_persona.setter
    # def id_persona(self, id_persona):
    #     self._id_persona = id_persona

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email

    def __str__(self) -> str:
        return f'''Persona: 
            id_persona: {self._id_persona}, nombre: {self._nombre}, 
            apellido: {self._apellido}, email: {self._email}'''


if __name__ == '__main__':

    unaPersona = Persona(1, 'Esteban', 'Pinti', 'epinti@gmail.com')
    log.debug(unaPersona)

    # Simulate a INSERT
    unaPersona = Persona(nombre='Enrique', apellido='Garcia', email='egarcia@gmail.com')
    log.debug(unaPersona)
    # print(f'{unaPersona} - {personaDos}')

    # Simular DELETE
    unaPersona = Persona(id=1)
    log.debug(unaPersona)
