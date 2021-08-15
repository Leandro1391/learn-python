# cantidad de argumentos que desconozco - con asterisco va recibir una tupla de elementos - una tupla es inmutable
# Docs - myFunctions(*args)
def listNames(*names):
    for name in names:
        print(name)

listNames('Angelo', 'Raffaelo', 'Naralia', 'Floro')
listNames('Luisa', 'Pedro')