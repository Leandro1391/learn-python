# Always we start with the class have not relation with other for example the class Product in the diagram UML

class Product:
    countProductos = 0

    #classmethod

    def __init__(self, name, price) -> None:
        Product.countProductos += 1
        self._idProduct = Product.countProductos
        self._name = name
        self._price = price

    @property
    def price(self):
        return self._price

    def __str__(self) -> str:
        return f'Id Product: {self._idProduct}, Name {self._name}, Price: {self._price}'

if __name__ == '__main__':
    prductoOne = Product('jacket', 250.00)
    prductoTwo = Product('Trousers', 520.00)