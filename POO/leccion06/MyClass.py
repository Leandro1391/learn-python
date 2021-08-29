class MyClass:
    # todo lo creado antes del init o afuera son variables de clase
    # Las variables de clase se asocia a la clase y se comparte con todos los objetos instaciados con este
    # y no es necesario crear una instancia de la clase para acceder a las variables o memtodos de clase

    # los metodos y atributos de instancia son independientes entre sí y no comparten información y para acceder lo tenemos que realizar una instancia de la clase

    variablesClass = 'Value variable class'

    def __init__(self, variableInstance):
        self.variableInstance = variableInstance

print(MyClass.variablesClass)
miClass = MyClass('Value variable instance')
print(miClass.variableInstance)

# Los objetos también se pueden acceder a las variables de clase
print(miClass.variablesClass)

# Se puede acceder a las variables de clase desde un objeto porque en primer lugar se carga la clase en memoria (Contexto Estático)
# y después al estar cargado en memoria podemos crear las instancias de las clases (objetos) (Contexto Dinámico)

miClass3 = MyClass('Other value variable instance')
print(miClass3.variableInstance)
print(miClass3.variablesClass)