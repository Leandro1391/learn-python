from Empleado import Empleado


class Gerente(Empleado):

    def __init__(self, name, sueldo, departamento) -> None:
        super().__init__(name, sueldo)
        self._departamento = departamento

    def __str__(self):
        return f'Gerente [Departamento: {self._departamento}] {super().__str__()}'