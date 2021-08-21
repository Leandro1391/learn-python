class Aritmetica:
    # Doc String
    '''
    Clase Aritmetica realiza las operaciones de sumar, restar, mutiplicar y dividir
    Los metodos take name actions
    '''
    
    def __init__(self, numberOne: int, numberTwo: int) -> None:
        self.numberOne = numberOne
        self.numberTwo = numberTwo

    def sum(self) -> int:
        return self.numberOne + self.numberTwo

    def subtract(self) -> int:
        return self.numberOne - self.numberTwo

    def mult(self) -> int:
        return self.numberOne * self.numberTwo

    def div(self) -> float:
        return self.numberOne / self.numberTwo



arithmeticOne = Aritmetica(5, 6)
print(f'La suma es: {arithmeticOne.sum()}')
print(f'La resta es: {arithmeticOne.subtract()}')
print(f'La multiplicacion es: {arithmeticOne.mult()}')
print(f'La division es: {arithmeticOne.div():.3f}')