
from Rectangulo import Rectangulo
from Cuadrado import Cuadrado

unCuadrado = Cuadrado(5, 'verde')
print(unCuadrado)
print(f'El area del rectangulo es: {unCuadrado.calcularAreaFigura()}')

unRectangulo = Rectangulo(5, 6, 'rosa')
print(unRectangulo)
print(f'El area del rectangulo es: {unRectangulo.calcularAreaFigura()}')