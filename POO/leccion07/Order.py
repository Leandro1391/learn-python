from Product import Product
from typing import List

class Order:

    countOrders: int = 0

    def __init__(self, products: List[Product]) -> None:
        Order.countOrders += 1
        self._idOrder: int = Order.countOrders
        self._listProductos = list(products)

    def addProduct(self, product):
        self._listProductos.append(product)

    def totalCalculate(self):
        total = 0
        for product in self._listProductos:
            total += product.price
        return total

    def __str__(self) -> str:
        productsStr = ''
        for product in self._listProductos:
                productsStr += product.__str__() + ' | '

        return f'Order; {self._idOrder}, Products: {productsStr}'


if __name__ == '__main__':
    print('I am here Order')
    productoOne = Product('jacket', 250.00)
    productoTwo = Product('Trousers', 520.00)
    products = [productoOne, productoTwo]
    orderOne = Order(products)
    print(orderOne)
    orderTwo = Order(products)
    print(orderTwo)