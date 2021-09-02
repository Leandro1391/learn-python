# Polimorfismo - Concepto basico: multiples formas o comportamientos en tiempo de ejecución

# La misma variable puede ejecutar varios metodos de distitos objetos dependiendo al objeto que está apuntando 
# en memoria en tiempo de ejecución

from typing import Union
from Empleado import Empleado
from Gerente import Gerente

def print_details(objectTest: Union[Empleado, Gerente]):
    print(objectTest)
    print(type(objectTest))
    objectTest.show_details()
    if isinstance(objectTest, Gerente):
        print(objectTest._departamento)

unEmpleado = Empleado('Pedro', 5000)
print_details(unEmpleado)

unGerente = Gerente('Julieta', 6000, 'Security')
print_details(unGerente)

# No es recomendable realizar muchas validaciones sobre los tipos en un metodo usando python si es una cuestión muy muy especifica podemos realizar una pequeña validación
# El metodo tiene que ser lo mas generico posible, tratar en lo posibles aplicar validaciones
# La narutaleza de puthon es trabajar con objetos en forma dinamica