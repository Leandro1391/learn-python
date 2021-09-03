class Computadora:

    contadorComputadoras: int

    def __init__(self, nombre: str, monitor, teclado, raton):
        self._idComputadora = Computadora.contadorComputadoras + 1
        self._nombre = nombre
        self._monitor = monitor
        self._teclado = teclado
        self._raton = raton

    @property
    def idComputadora(self):
        return self._idComputadora

    @idComputadora.setter
    def idComputadora(self, idComputadora):
        self._idComputadora = idComputadora

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def monitor(self):
        return self._monitor

    @monitor.setter
    def monitor(self, monitor):
        self._monitor = monitor

    @property
    def teclado(self):
        return self._teclado

    @teclado.setter
    def teclado(self, teclado):
        self._teclado = teclado

    @property
    def raton(self):
        return self._raton

    @raton.setter
    def raton(self, raton):
        self._raton = raton

    def __str__(self) -> str:
        return f'Computadora: [idComputadora {self._idComputadora}, nombre {self._nombre}, monitor {self._monitor}, teclado {self._teclado}, raton {self._raton}]'