from DispositivoEntrada import DispositivoEntrada

class Raton(DispositivoEntrada):

    contadorMouses: int = 0

    def __init__(self, marca: str, tipoEntrada: str):
        super().__init__(marca, tipoEntrada)
        self._idRaton = Raton.contadorMouses + 1
        Raton.contadorMouses = self._idRaton

    @property
    def idRaton(self):
        return self._idRaton

    @idRaton.setter
    def idRaton(self, idRaton):
        self._idRaton = idRaton

    def __str__(self) -> str:
        return f'Raton: id: {self._idRaton} {super().__str__()}'

    
if __name__ == '__main__':
        unRaton = Raton('Lenovo', 'usb')
        print(unRaton)
        