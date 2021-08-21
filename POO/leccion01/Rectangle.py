class Rectangle:

    def __init__(self, base, height) -> None:
        self.base = base
        self.height = height

    def calculateArea(self):
        return self.base * self.height

base = int(input('Ingresar la base: '))
height = int(input('Ingresar la altura: '))

aRectangle = Rectangle(base, height)
print(f'Area del rectangulo es: {aRectangle.calculateArea()}')