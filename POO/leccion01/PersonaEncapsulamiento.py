# https://umletino.com/umletino.html

from typing import Union

# Todo atributo con guion bajo en la clase significa que esta encapsulado


class PersonaEncapsulamiento:

    def __init__(self, name, familyName, age) -> Union[str,int]:
        self._name = name
        self.familyName = familyName
        self.age = age

    # GET - decorator poperty - los decoradores modifican el compotamiento del metodo get
    @property
    def name(self):
        return self._name

    # SET
    @name.setter
    def name(self, name):
        self._name = name

    def show_details(self):
        print(f'Persona: {self._name} {self.familyName} {self.age}')

person1 = PersonaEncapsulamiento('Rosa', 'Paglione', 35)
print(person1.name)
person1.name = 'Gabriel Pedro'
print(person1.name)


# Esta forma es incorrecta se deve setear a través de un metodo
# person1._name = 'Juan Schivi'
# person1.show_details()

        
# Encapsulamiento en python: Para encapsular se usa como anotación el guion bajo en una variable (_name) indicando que solamente se
# puede llamar ese atributo en la misma clase y no afuera, pero, no es restrictivo, es decir, que si lo llamo por afuera de la clase
# puedo cambiar el valor del atributo

# Para que no se pueda cambiar en forma restrictiva (aqunque no se usa mucho, lo normar es usar un guión bajo) es aplicar doble guion
# bajo, self.__name, con esa indicación no voy a poder invocar el atributo afuera de la clase