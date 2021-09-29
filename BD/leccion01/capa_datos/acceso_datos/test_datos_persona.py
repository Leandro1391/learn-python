# from Persona import Persona
from PersonaDao import PersonaDao

while True:

    opcion = int(input("""
    Seleccione una opción del 1 al 5:
    1 - Consulta la lista de personas
    2 - Agregar una persona
    3 - Actualizar los datos de una persona
    4 - Eliminar una persona
    5 - Salir
    """))

    if opcion == 1:
        PersonaDao.seleccionar()
    elif opcion == 2:
        name = str(input('Ingrese nombre:' ))
        familyName = str(input('Ingrese apellido:' ))
        email = str(input('Ingrese email:' ))

        unaPersona = PersonaDao(name, familyName, email)
        unaPersona.insertar()

    elif opcion == 5:
        print('break while')
        break
    else:
        print('else condition')
        