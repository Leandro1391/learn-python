from typing import List
from Computadora import Computadora

class Orden:

    contadorOrdenes: int = 0

    def __init__(self, computadoras: List[Computadora]):
        self._idOrden = Orden.contadorOrdenes + 1
        self._computadoras = list(computadoras)
        Orden.contadorOrdenes = self._idOrden

    @property
    def idOrden(self):
        return self._idOrden

    @idOrden.setter
    def idOrden(self, idOrden):
        self._idOrden = idOrden

    @property
    def computadoras(self):
        return self._computadoras

    @computadoras.setter
    def computadoras(self, computadoras):
        self._computadoras.append(computadoras)

    def agregarComputadora(self, computadora):
        self._computadoras.append(computadora)

    # def getListComputadoras(self):
    #     txt: str = ''
    #     for item in reversed(self._computadoras):
    #         txt = f'HP: {item.idComputadora}\n\t\t {item.monitor}\n\t\t {item.teclado}\n\t\t {item.raton}\n\t {txt}'
    #     return txt

    def __str__(self) -> str:
        # return f'Orden: {self._idOrden}, Computadoras:\n\t {self.getListComputadoras()}'
        computadorasStr = ''
        for computadora in self._computadoras:
            computadorasStr += computadora.__str__()

        return f'''
Orden: {self._idOrden}
Computadoras: {computadorasStr}
        '''

if __name__ == '__main__':
    unaOrdem = Orden()