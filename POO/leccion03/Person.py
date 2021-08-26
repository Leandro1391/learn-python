# Todas las clases heredan en forma directa o indirecta de la clase object
class Person(object):
    def __init__(self, name: str, age: int) -> None:
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    # Override
    def __str__(self) -> str:
        return f'Clase padre str: {super().__str__()} - Override child Persona[Nombre: {self._name}, edad: {self._age}]'

class Employed(Person):
    def __init__(self, name, age, sueldo:float) -> None:
        super().__init__(name, age)
        self._sueldo = sueldo

    @property
    def sueldo(self):
        return self._sueldo

    @sueldo.setter
    def sueldo(self, sueldo):
        self._sueldo = sueldo

    def __str__(self) -> str:
        return f'{super().__str__()} Empleado: [Sueldo: {self._sueldo}]'

        

employed1 = Employed('Jose', 20, 5000)
print(employed1.age)