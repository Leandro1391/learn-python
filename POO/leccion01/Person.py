# pass solamente va crear el metodo clase o consutructor sin ningun contenido
# con la palabra reservada pass solamente indicamos que no se va a procesar nada en la clase persona solamente crea
# el tipo de dato

from typing import Union


class Person:
    # pass

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
        

# print(type(Person))

# This is the invoke contructor for create object
personOne = Person('Carla', 'Videla', 40)
print(f'Object Memory Reference: {personOne}')
print(f'Person name: {personOne.name}')
print(f'Person Family Name: {personOne.familyName}')
print(f'Person age: {personOne.age}')