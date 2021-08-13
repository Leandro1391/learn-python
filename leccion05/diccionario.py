# Diccionario

# En python se puede almacenar elementos guardando en una key o indice los valores que se va asociar a la llave

# Example
# dict key      element
#      "IDE"    "Integrated Development Environment"
#      "OOP"    "Object Oriented Programming"
#      "DBMS"    "Database Managment System"

# dict (key, value)
# en la llave se pude usar cualquier tipo 'String', Int, etc
diccionario = {
    'IDE' : 'Integrated Development Environment',
    'OOP' : 'Object Oriented Programming',
    'DBMS' : 'Database Managment System'
}
print(diccionario)

# Length
print(len(diccionario))

# Para acceder al elemento del diccionario debemos especificar el valor de la llave que contiene el elemento
print(diccionario['IDE'])

# Another way to access an elemnt
print(diccionario.get('OOP'))

# Modificar elementos
diccionario['IDE'] = 'integrated development enviroment'
print(diccionario)

# Recorrer los elementos en un dicionario
for termino, element in diccionario.items():
    print(termino, element)

# Solamente me trae las llaves
for termino in diccionario.keys():
    print(termino)

# Me trae los valores asociados a las llaves
for values in diccionario.values():
    print(values)

# Comprobar la existencia de algún elemento
print('IDE' in diccionario)

# Throw error because don't exist
print('ide' in diccionario)

# Agregar un elemento - IMPORTANTE: no se puede agregar llaves duiplicados, si agregamos un elemento asociado con la llave duplicada
# sobreescribe su valor
diccionario['PK'] = 'Primary Key'
print(diccionario)

# Remover un elemento
diccionario.pop('DBMS')
print(diccionario)

# Para limpiar el diccionario sin eliminar la variable diccionario, es decir, variar todos su contenido como un truncate
diccionario.clear()
print(diccionario)

# Para eliminar por completo la variable en memoria
del diccionario
print(diccionario)

