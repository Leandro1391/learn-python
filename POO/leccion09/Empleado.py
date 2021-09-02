class Empleado:
    def __init__(self, name, sueldo) -> None:
        self._name = name
        self._sueldo = sueldo

    def __str__(self):
        return f'Empleado [Name: {self._name}, Sueldo: {self._sueldo}]'

    def show_details(self):
        print(self.__str__())