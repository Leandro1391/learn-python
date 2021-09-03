from DispositivoEntrada import DispositivoEntrada

class Teclado(DispositivoEntrada):

    def __init__(self, tipoEntrada, marca, idTeclado):
        super().__init__(tipoEntrada, marca)
        self._idTeclado = idTeclado

    @property
    def idTeclado(self):
        return self._idTeclado

    @idTeclado.setter
    def idTeclado(self, idTeclado):
        self._idTeclado = idTeclado

    def __str__(self) -> str:
        return f'Teclado: [idTeclado {self._idTeclado}] {super().__str()}'