x = 10
print(x)
# Con type puedo saber que tipo de dato es la variable x
print(type(x))
# <class 'int'>

x = 'Hello   World'
print(x)
# <class 'string'>
print(type(x))

# Las variables pueden apuntar a cualquier tipo de dato
# la palabra reservada hint: no definde el tipo de dato que va alamcenar la variable
# Con hint = pusta o indicación podemos indicar cual es tipo que apunta la variablre

y: str = 'Hello moto'
print(y)
print(type(y))
# Aclaración: el hint no define que la variable solamente puede almacenar datos de tipo string, solamente es una INDICACION
# para saber el tipo de dato que puede estar almacenando,
# las variables en python son DINAMICAS pueden cambiar

x = 10.5
print(x)
print(type(x))

x = True
print(x)
print(type(x))

# Python es un lenguaje orientado a objetos, por lo tanto, son las clases las encargadas que van almacenar la informacion
# A su vez los tipos de datos son clases, por eso en el print por consola se ve la palabra 'class'
# Todos los datos van a estar almacenados en clases en Python