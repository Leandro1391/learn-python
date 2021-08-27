class FiguraGeometrica:

    def __init__(self, alto, ancho) -> None:
        self._alto = alto
        self._ancho = ancho

    @property
    def get_alto(self):
        return self._alto

    @get_alto.setter
    def set_alto(self, alto):
        self._alto = alto

    @property
    def get_ancho(self):
        return self._ancho

    @get_ancho.setter
    def set_ancho(self, ancho):
        self._ancho = ancho

    def __str__(self) -> str:
        # return f'{super().__str__()}, Figura geometrica: [alto: {self._alto}, ancho: {self._ancho}]'
        return f'Figura geometrica: [alto: {self._alto}, ancho: {self._ancho}]'

    