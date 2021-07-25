x = 10
y = 2
z = x + y
print(x)
print(y)
print(z)
# Los siguientes prints muestra donde está guardado en la posicion de direccion de memoria ram cada una de las variables
# variables x y z, para saber el valor de la direccion de memoria tenemos que usar la funcion id
print(id(x))
print(id(y))
print(id(z)) # -> el numero que se ve en consola también se llama Referencia de Memoria o simplemente Referencia
print("El resultado es: " + str(z))

# Los valores de las variables se almacenan en una posición de la memoria ram o en una dirección de memoria
# cada número o valor que vamos a almacenar en la variable se llama literal
# una literal es un valor que le podemos asignar a nuestras variables, como por ejemplo, la literal 10