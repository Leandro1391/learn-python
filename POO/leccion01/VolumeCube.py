class Cube:

    def __init__(self, long, high, deep) -> None:
        self.long = long
        self.high = high
        self.deep = deep

    def calculateVolume(self):
        return self.long * self.high * self.deep

long = int(input('Ingrese largo: '))
high = int(input('Ingrese altura: '))
deep = int(input('Ingrese profundidad: '))

aCube = Cube(long, high, deep)
print(f'Volumen del cubo es: {aCube.calculateVolume()}')