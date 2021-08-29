# Las clases abstractas sirve para implementar metodos abstractos y esto obliga implementar a las clases hijas, pero en la
# clase padre no se implementa, solamente creamos la firma del metodo abstracto (por ejemplo calcularArea()) y también
# al definir a la clase padre como abstracto NO se podra crear instancias del mismo al ser una clase abstract

#ABC = Abstract Base Class
from abc import ABC, abstractmethod


class FiguraGeometrica(ABC):

    def __init__(self, alto, base) -> None:
        if self._validate_value(alto):
            self._alto = alto
        else:
            self._alto = 0
            print('Error el valor ingresado para la altura')
        if self._validate_value(base):
            self._base = base
        else:
            self._base = 0
            print('Error el valor ingresado para la base')

    @property
    def alto(self):
        return self._alto

    @alto.setter
    def alto(self, alto):
        if self._validate_value(alto):
            self._alto = alto
        else:
            print(f'Valor erroneo base: {alto}')


    @property
    def base(self):
        return self._base

    @base.setter
    def base(self, base):
        if self._validate_value(base):
            self._base = base
        else:
            print(f'Valor erroneo base: {base}')

    @abstractmethod
    def calcularAreaFigura(self):
        pass


    def __str__(self) -> str:
        # return f'{super().__str__()}, Figura geometrica: [alto: {self._alto}, base: {self._base}]'
        return f'Figura geometrica: [alto: {self._alto}, base: {self._base}]'

    def _validate_value(self, value):
        return True if 0 < value < 10 else False