# send list in argument
def showNames(names):
    for name in names:
        print(name)

showNames(['Carolina', 'Vicenta', 'Ramona'])
showNames(['Julia'])
showNames('Jose Maria')
# showNames(10) -> los enteros no son iterables
# showNames(10, 11) -> La funcion solamente recibe un argumento

# tupla
showNames((10, 11))

# Listas
showNames([10, 11])
