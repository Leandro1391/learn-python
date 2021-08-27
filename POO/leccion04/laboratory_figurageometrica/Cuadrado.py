from FiguraGeometrica import FiguraGeometrica
from Color import Color

class Cuadrado(FiguraGeometrica, Color):
    def __init__(self, lado, color) -> None:
        FiguraGeometrica.__init__(self, lado, lado)
        Color.__init__(self, color)

    def calcularAreaFigura(self):
        return self.set_alto * self.set_ancho

    def __str__(self) -> str:
        # return f'{super().__str__()}'
        return f'{FiguraGeometrica.__str__(self)}, {Color.__str__(self)}'