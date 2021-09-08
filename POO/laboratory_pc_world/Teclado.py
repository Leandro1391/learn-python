from DispositivoEntrada import DispositivoEntrada

class Teclado(DispositivoEntrada):

    contadorTeclados: int = 0

    def __init__(self, marca: str, tipoEntrada: str):
        super().__init__(marca, tipoEntrada)
        self._idTeclado = Teclado.contadorTeclados + 1
        Teclado.contadorTeclados = self._idTeclado

    @property
    def idTeclado(self):
        return self._idTeclado

    @idTeclado.setter
    def idTeclado(self, idTeclado):
        self._idTeclado = idTeclado

    def __str__(self) -> str:
        return f'Teclado: id {self._idTeclado} {super().__str__()}'

if __name__ == '__main__':
        unTeclado = Teclado('usb' ,'Lenovo')
        print(unTeclado)