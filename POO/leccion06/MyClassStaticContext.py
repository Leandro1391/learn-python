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
    # Un METODO ESTATICO NO CONTIENE INFORMACION DE NUESTRA CLASE, 
    # Sirve para asociar de manera logica un atributo o metodo que no pertenezca a nuestra clase, no tiene informacion extra de nuestra clase
    @staticmethod
    def methodStatic():
        MyClass.variableClass
        # En el metodo estatico no se puede inicializar variables o atributos de instancia porque el metodo pertenece al contexto estático y se crean antes
        # que los objetos en memoria, no tiene la palabra reservada self

    # METODOS CLASE
    # recibe un contexto de clase parecido al self pero en el contexto estático (parámetro cls)
    @classmethod
    def methodClass(cls):
        print(cls.variableClass)


MyClass.methodClass()  


# Acceso al metodo estatico
MyClass.methodStatic()


#Un metodo estatico no recibe una referencia de nuestra clase y por lo tanto no contiene nninguna información de nuestra clase
# para acceder a los atributos de la clase tenemos que acceder mediante el nombre del mismo

# Metodo de clase recibe la información de la misma y podemos acceder sus atributos o metodo con el parametro cls
