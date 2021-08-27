from FiguraGeometrica import FiguraGeometrica
from Color import Color

class Rectangulo(FiguraGeometrica, Color):
    def __init__(self, alto, ancho, color) -> None:
        FiguraGeometrica.__init__(self, alto, ancho)
        Color.__init__(self, color)

    def calcularAreaFigura(self):
        return self.alto * self.base

    def __str__(self) -> str:
        # return f'{super().__str__()}'
        return f'{FiguraGeometrica.__str__(self)}, {Color.__str__(self)}'