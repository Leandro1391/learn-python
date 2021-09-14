class Pelicula:

    def __init__(self, name: str):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    def __str__(self) -> str:
        return f'Pelicula: {self._name}'

if __name__ == '__main__':
    unaPeli = Pelicula('Batman')
    print(unaPeli)
    