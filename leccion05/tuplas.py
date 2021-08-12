 # Una lista es MUTABLE, es decir, que es modificable (append, inser, remove, pop)

 # Las tuplas son parecidos a las listas pero es INMUTABLE, es decir, no se puede modificar, eliminar y/o agregar
 # elementos

 # Definir tupla
frutas = ('Orange', 'Banana', 'Strawerry')
print(frutas)

# Saber el largo de la tupla
print(len(frutas))

# Acceder a un elemento
print(frutas[0])

# navegacion inversa
print(frutas[-1])

# acceder a un rango de valores
print(frutas[0:1]) # sin incluir el último índice
# IMPORTANTE si vamos a declarar una tupla de un solo elemento tenemos que declarar de la siguiente forma
exampleTuples = ('test',) # tenemos que agregar una coma al final o sino lo va tomar como un string

# Recorrer tuplas
for fruta in frutas:
    print(fruta, end=' ') # end es un argumento propio de print

# Las tuplas son inmutables por ejemplo
# frutas[0] = 'Pera'

# Pero podemos cambiar un tipo tupla a lista para poder modificar sus valores
frutasLista = list(frutas)
frutasLista[0] = 'Pera'
frutas = tuple(frutasLista)
print('\n', frutas)

# Siempre es bueno que desde el inicio del proyecto definir si usa una tupla o lista para almacenar elemtos para no realizar las estas conversiones
# si se va por el lado de listas es porque se va a poder editar sus valores (dinámico)
# si se va por el la de las tuplas significa que no se van a modificar sus valores (estático)

# eliminar tupla por completo
del frutas
print(frutas)
