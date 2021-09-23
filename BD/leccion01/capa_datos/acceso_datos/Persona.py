
class Persona:

    contador: int = 0

    def __init__(self, nombre, apellido, email):
        Persona.contador += 1
        self._id_persona = Persona.contador
        self._nombre = nombre
        self._apellido = apellido
        self._email = email

    @property
    def id_persona(self):
        return self._id_persona

    @id_persona.setter
    def id_persona(self, id_persona):
        self._id_persona = id_persona

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
        return f'Persona: [id_persona {self._id_persona}, nombre {self._nombre}, apellido {self._apellido}, email {self._email}]'


if __name__ == '__main__':

    unaPersona = Persona('Esteban', 'Pinti', 'epinti@gmail.com')
    personaDos = Persona('Enrique', 'Garcia', 'egarcia@gmail.com')
    print(f'{unaPersona} - {personaDos}')
