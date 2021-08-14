# Una función es un bloque de codigo que lo vamos a poder a invocar n cantidad de veces, en la cual, podemos implementar
# la logica que necesitamos para que lo procese


#IMPORTANTE las variables son dinamicas en python
# camelCase
# Los parámetros son las variables que declaremos en nuestra funcion
def myFunctionInPython(name, lastname):
    print('Greeting from my python function')
    print(f'Nombre: {name}, Apellido: {lastname}')

# El argumento es el valor que enviamos a la funcion, en este caso Leandro y Julian son argumentos
myFunctionInPython('Leandro', 'Julian')
myFunctionInPython('Rebeca', 'Francesca')


# Another way
# def my_function_python():