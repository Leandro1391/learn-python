# Los elementos del CONTEXTO DINAMICO pueden accedera los elementos del CONTEXTO ESTATICO, pero no sucede lo mismo al viceversa porque lo primero que se carga en memoria son los atributos y metodos de clase y los objetos se cargan a lo ultimo
# Ejemplo SO (estático) y Buscaminas (objeto - dinamico)

class MyClass:
    # todo lo creado antes del init o afuera son variables de clase
    # Las variables de clase se asocia a la clase y se comparte con todos los objetos instaciados con este
    # y no es necesario crear una instancia de la clase para acceder a las variables o memtodos de clase

    # los metodos y atributos de instancia son independientes entre sí y no comparten información y para acceder lo tenemos que realizar una instancia de la clase

    variableClass = 'Value variable class'

    def __init__(self, variableInstance):
        self.variableInstance = variableInstance

    # METODOS ESTATICOS: Se asocian a la clase igual que una variable de clase, no pueden acceder a los metodos y atributos de instancia 
    # porque los metodos estaticos se cargan en memoria en el momento que se crea por primera vez la instancia de la clase u OBJETO, 
    # NUNCA SE CREARA ANTES LOS METODOS ESTATICOS qie los objetos
    @staticmethod
    def methodStatic():
        MyClass.variableClass
        # En el metodo estatico no se puede inicializar variables o atributos de instancia porque el metodo pertenece al contexto estático y se crean antes
        # que los objetos en memoria, no tiene la palabra reservada self

    # METODOS CLASE
    @classmethod
    def methodClass(cls):
        print(cls.variableClass)


MyClass.methodClass()  



# Acceso al metodo estatico
MyClass.methodStatic()

# self hace referencia a objetos


print(MyClass.variableClass)
miClass = MyClass('Value variable instance')
print(miClass.variableInstance)

# Los objetos también pueden acceder a las variables de clase
print(miClass.variableClass)

# Como python es un lenguaje dinamico y todos los tipos de datos son objetos => es posible crear atributos en vuelo
MyClass.variableClaseFly2 = 'Value cariable class 2'

# Se puede acceder a las variables de clase desde un objeto porque en primer lugar se carga la clase en memoria (Contexto Estático)
# y después al estar cargado en memoria podemos crear las instancias de las clases (objetos) (Contexto Dinámico)

miClass3 = MyClass('Other value variable instance')
print(miClass3.variableInstance)
print(miClass3.variableClass)


print('***********************')
print(miClass.variableClaseFly2)
print(miClass3.variableClaseFly2)