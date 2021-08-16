# listNumber = []
# def descendentNaturalNumber(number:int = 0):
#     if number == 0:
#         return listNumber
#     elif number > 0:
#         listNumber.append(number)
#         return descendentNaturalNumber(number-1)
#     else:
#         return ''

# inputNumber = 5
# print(f'Los numeros naturales descendentes de {inputNumber} son: {descendentNaturalNumber(inputNumber)}')


# def descendentNaturalNumber(number:int = 0):
#     if number == 0:
#         return 1
#     elif number > 0:
#         print(number)
#         return descendentNaturalNumber(number-1)
#     else:
#         return ''

# descendentNaturalNumber(5)
# print(f'\n')
# descendentNaturalNumber(3)
# print(f'\n')
# descendentNaturalNumber(-5)

# the bes way

def imprimir_numero_recursivo(numero):
    if numero >= 1:
        print(numero)
        imprimir_numero_recursivo(numero-1)

imprimir_numero_recursivo(5)