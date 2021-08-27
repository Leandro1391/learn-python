
from Rectangulo import Rectangulo
from Cuadrado import Cuadrado


print('Creación Objeto Cuadrado:'.center(50,'-'))
unCuadrado = Cuadrado(5, 'verde')
unCuadrado.alto = 9
print(unCuadrado)
print(f'El area del cuadrado es: {unCuadrado.calcularAreaFigura()}')

print('Creación Objeto Rectangulo:'.center(50,'-'))
unRectangulo = Rectangulo(5, 6, 'rosa')
print(unRectangulo)
print(f'El area del rectangulo es: {unRectangulo.calcularAreaFigura()}')