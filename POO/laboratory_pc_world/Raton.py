from DispositivoEntrada import DispositivoEntrada

class Raton(DispositivoEntrada):

    def __init__(self, tipoEntrada, marca, idRaton):
        super().__init__(tipoEntrada, marca)
        self._idRaton = idRaton

    @property
    def idRaton(self):
        return self._idRaton

    @idRaton.setter
    def idRaton(self, idRaton):
        self._idRaton = idRaton

    def __str__(self) -> str:
        return f'Raton: [idRaton {self._idRaton}] {super().__str()}'