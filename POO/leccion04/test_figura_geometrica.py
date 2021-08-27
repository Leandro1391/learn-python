from Cuadrado import Cuadrado

cuadrado1 = Cuadrado(6, 'azul')
print(cuadrado1.alto)
print(cuadrado1.ancho)
print(cuadrado1.color)
print(f'El calculo del area del cuadrado es: {cuadrado1.calcularArea()}')

print(cuadrado1)

# En herencia mutiple es importante saber cual orden que se ejeucan las clases padres
# para eso usamosMRO - Method Resolution Order
print(Cuadrado.mro()) # -> [<class 'Cuadrado.Cuadrado'>, <class 'FiguraGeometrica.FiguraGeometrica'>, <class 'Color.Color'>, <class 'object'>]

# Primer la hija (Cuadrado) -> 2do clase padre FiguraGeometrica -> 3ro clase padre Color -> 4to clase object