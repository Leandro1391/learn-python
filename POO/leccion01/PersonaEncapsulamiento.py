# https://umletino.com/umletino.html


# Todo atributo con guion bajo en la clase significa que esta encapsulado


class PersonaEncapsulamiento:

    def __init__(self, name, familyName, age):
        self._name = name
        self._familyName = familyName
        self._age = age


    # GET - decorator poperty - los decoradores modifican el compotamiento del metodo get
    @property
    def name(self):
        return self._name

    # para crear variables de solo lectura no debo crear la propiedad setter

    # SET name
    @name.setter
    def name(self, name):
        self._name = name
    
    # GET familyName
    @property
    def familyName(self):
        return self._familyName

    # SET familyName
    @familyName.setter
    def familyName(self, familyName):
        self._familyName = familyName

    # GET age
    @property
    def age(self):
        return self._age

    # SET age
    @age.setter
    def age(self, age):
        self._age = age    

    def show_details(self):
        print(f'Persona: {self._name} {self._familyName} {self._age}')

    # Todos los objetos en python heredan de la clase OBJECT
    def __del__(self):
        print(f'Person: {self._name} {self._familyName}')


# Con esto validamos que no ejecute este test en otro modulo o archivo
if __name__ == '__main__':
    person1 = PersonaEncapsulamiento('Rosa', 'Paglione', 35)
    print(person1.name)
    person1.name = 'Gabriel Pedro'
    print(person1.name)

    person1.age = 54
    print(person1.age)

    person1.familyName = 'Gilberto'
    print(person1.familyName)

    person1.show_details()

    print(__name__)


# Esta forma es incorrecta se deve setear a través de un metodo
# person1._name = 'Juan Schivi'
# person1.show_details()

        
# Encapsulamiento en python: Para encapsular se usa como anotación el guion bajo en una variable (_name) indicando que solamente se
# puede llamar ese atributo en la misma clase y no afuera, pero, no es restrictivo, es decir, que si lo llamo por afuera de la clase
# puedo cambiar el valor del atributo

# Para que no se pueda cambiar en forma restrictiva (aqunque no se usa mucho, lo normar es usar un guión bajo) es aplicar doble guion
# bajo, self.__name, con esa indicación no voy a poder invocar el atributo afuera de la clase