# Una lista es un conjunto de elementos pueden ser tipos de string u otros
# Cada elemento de lista se le asigna un indice
# Para definir una lista usamos corchetes

# nombre = ["Juan", "Karla", "Ricardo", "Maria"]

# Para no ocupar tanto espacio usaremos comillas simples
# También en una misma lista podemos declarar otros tipos enteros, booleano, etc

# Definir una lista de tipo str
nombres = ['Juan', 'Karla', 'Ricardo', 'Maria']
# Imprimi la lista de nombres
print(nombres)
# acceder a los elementos de una lista
print(nombres[0])
print(nombres[1])

# acceder a los elementos de forma inversa
print(nombres[-1])
print(nombres[-2])

#Imprimir un rango
print(nombres[0:2]) # no incluimos el indice 3

# Ir del inico de la lista al indice (sin incluirla)
print(nombres[:3])

# Desde el indice indicado hast el final de nuestra lista
print(nombres[1:])

# Cambios de un valor
nombres[3] = 'Natalia'
print(nombres)

#Iterar una Lista
for nombre in nombres:
    print(f'nombre: {nombre} - indice: {nombres.index(nombre)}')
else:
    print('No existe mas nombres en la lista')

# Ask the list's length array
print(len(nombres))

# agregar un elemento -> el operador punto nos permite acceder a los métodos o funciones de una lista
nombres.append('Floro')
print(nombres)

# Insertar un elemento en un indice específico
nombres.insert(2, 'Mennato')
print(nombres)

# Remover un elemento de la lista
nombres.remove('Karla')
print(nombres)

# Remover el último elemento de la lista
nombres.pop()
print(nombres)

# Eleminar un indici especifico
del nombres[0]
print(nombres)

# Limpiar la lista
nombres.clear()
print(nombres)

# Borrar la Lista por completo, es decir, lo borramos de la memoria
del nombres
print(nombres )