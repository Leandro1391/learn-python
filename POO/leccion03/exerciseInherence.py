class Vehiculo():
    def __init__(self, color, ruedas) -> None:
        self._color = color
        self._ruedas = ruedas

    # investigar getter
    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color

    @property
    def ruedas(self):
        return self._ruedas

    @ruedas.setter
    def ruedas(self, ruedas):
        self._ruedas = ruedas

    def __str__(self) -> str:
        return f'color: {self._color}, ruedas {self._ruedas}'

class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad) -> None:
        super().__init__(color, ruedas)
        self._velocidad = velocidad

    @property
    def velocidad(self):
        return self._velocidad

    @velocidad.setter
    def velocidad(self, velocidad):
        self._velocidad = velocidad

    def __str__(self) -> str:
        return f'{super().__str__()} - Velocidad: {self._velocidad} Km/h'

class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo) -> None:
        super().__init__(color, ruedas)
        self._tipo = tipo

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, tipo):
        self._tipo = tipo

    def __str__(self) -> str:
        return f'{super().__str__()} - Tipo: {self._tipo}'


unaBicicleta = Bicicleta('rojo', 2, 'montainbike')
print(unaBicicleta)

unCoche = Coche('azul', 4, 120)
print(unCoche)