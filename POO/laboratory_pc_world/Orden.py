class Orden:

    contadorOrdenes: int = 0

    def __init__(self):
        self._idOrden = Orden.contadorOrdenes + 1

    @property
    def idOrden(self):
        return self._idOrden

    @idOrden.setter
    def idOrden(self, idOrden):
        self._idOrden = idOrden

    def __str__(self) -> str:
        return f'Orden: [idOrden {self._idOrden}]'