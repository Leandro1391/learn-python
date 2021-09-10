class HandleFiles:

    def __init__(self, name: str):
        self._name = name

    def __enter__(self):
        print('Get the resource'.center(50,'-'))
        self._name = open(self._name, 'r', encoding='utf8')
        return self._name

    # traceback es toda la lista de errores si es que ocurrió alguno
    # se debe cumplir con la siguiente firma del metodo exit porque sino devuelve error el compilador al ejecutar
    def __exit__(self, type_exception, value_exception, traceback):
        print('Close the resource'.center(50,'-'))
        if self._name:
            self._name.close()
        

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

        

    def __str__(self) -> str:
        return f'HandleFiles: [name {self._name}]'