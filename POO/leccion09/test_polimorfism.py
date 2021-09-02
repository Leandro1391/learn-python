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

unEmpleado = Empleado('Pedro', 5000)
print_details(unEmpleado)

unGerente = Gerente('Julieta', 6000, 'Security')
print_details(unGerente)