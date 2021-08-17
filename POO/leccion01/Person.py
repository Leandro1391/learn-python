# https://umletino.com/umletino.html

# pass solamente va crear el metodo clase o consutructor sin ningun contenido
# con la palabra reservada pass solamente indicamos que no se va a procesar nada en la clase persona solamente crea
# el tipo de dato

# Los ATRIBUTOS son las caracteristicas que nuestros objetos van a tener al momento de crearlos con instancia de la clase
# Los METODOS son los comportamientos que van a tener nuestros objeto

from typing import Union


class Person:
    # pass

    # Aquí pdoemos crear los atributos de clase

    # Contructor inicializa los atirbutos del objeto pero realmente está oculto en python
    # self es como la palabra reservada this, es decir, una referencia al mismo objeto donde podremos acceder sus atributos y metodos
    # method dunder init o double underscore o tambien llamado metodo especial o tipo dunder en python
    def __init__(self, name, familyName, age) -> Union[str,int]:
        # Iniciamos los atributos de instancia
        self.name = name
        self.familyName = familyName
        self.age = age

    # def __str__(self) -> str:
    #     pass

    # def __repr__(self) -> str:
    #     pass

    # todos los metodos de instancia va a recibir el parametro self -> se van asociar a los objetos creados
    def show_details(self):
        print(f'Persona: {self.name} {self.familyName} {self.age}')
        

# print(type(Person))

# This is the invoke contructor for create object
personOne = Person('Carla', 'Videla', 40)
print(f'Object Memory Reference: {personOne}')
print(f'Person Object 1: {personOne.name} {personOne.familyName} {personOne.age}')
# print(f'Person name: {personOne.name}')
# print(f'Person Family Name: {personOne.familyName}')
# print(f'Person age: {personOne.age}')

personTwo = Person('Pablo', 'Gerez', 68)
print(f'Object Memory Reference: {personTwo}')
print(f'Person Object 2: {personTwo.name} {personTwo.familyName} {personTwo.age}')
# print(f'Person name: {personTwo.name}')
# print(f'Person Family Name: {personTwo.familyName}')
# print(f'Person age: {personTwo.age}')

# La clase es la plantilla o el molde donde a partir de esto creamos los objetos
# La clase es donde nos va a permitir definir las características y comportamientos del objeto

# modified values in objects (esto no es recomendable, usar getters y setters - encapsulamiento)
personOne.name = 'Ramona'
personOne.familyName = 'Ramoes'
personTwo.age = 32
print(f'Person Object 1: {personOne.name} {personOne.familyName} {personOne.age}')
print(f'Person Object 2: {personTwo.name} {personTwo.familyName} {personTwo.age}')

personOne.show_details()
personTwo.show_details()