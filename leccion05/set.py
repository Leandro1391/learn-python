# Un set es una collecion de datos con la siguiente caracteristicas:

# 1. No mantiene un orden (No posee indices)
# 2. No permite almacenar elementos duplicados
# 3. No se permite modificar los elementos almacenados
# 4. Permite agregar o eliminar elementos

planets = {'Mars', 'Jupiter', 'Venus'}
print(planets)

# Length of elements
print(len(planets))

# Revisar si un elemento esta presente (ESTO TAMBIEN SE USA EN TUPLAS Y LISTAS)
print('Mars' in planets)

# Add a element
planets.add('Earth')
print(planets)

# Not allow duplicate elements
planets.add('Earth')
print(planets)

# Remove a element - Throw error if doesn't find an element
# planets.remove('Earth')
# print(planets)

# La funcion discard también elimina un elemento en el set y no arroja error si no lo encuentra
planets.discard('Earh')

# para eliminar todos los elementos del SET usamos el keyword del
del planets
print(planets)
