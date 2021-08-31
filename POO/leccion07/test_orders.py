from Order import Order
from Product import Product


productOne = Product('jacket', 250.00)
productTwo = Product('Trousers', 520.00)
productThree = Product('shoes', 800.00)
productFour = Product('sockets', 600.00)

productsOne = [productOne, productTwo]
productsTwo = [productThree, productFour]
orderOne = Order(productsOne)
orderOne.addProduct(productThree)
orderOne.addProduct(productFour)
print(orderOne)
print(f'Total de la orden1: {orderOne.totalCalculate()}')

orderTwo = Order(productsTwo)
print(orderTwo)
print(f'Total de la orden2: {orderTwo.totalCalculate()}')

