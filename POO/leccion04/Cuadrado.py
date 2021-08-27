from FiguraGeometrica import FiguraGeometrica
from Color import Color


class Cuadrado(FiguraGeometrica, Color):
    def __init__(self, lado, color) -> None:
        # super().__init__(lado) -> solamente va ejecutar la primera clase padre en el argumento
        FiguraGeometrica.__init__(self, lado, lado)
        Color.__init__(self, color)

    def calcularArea(self):
        return self.alto * self.ancho

    def __str__(self) -> str:
        return f'{super().__str__()}'
