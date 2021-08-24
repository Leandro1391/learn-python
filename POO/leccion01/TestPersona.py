# un archivo o modulo puede tener mas de una clase - para traer todas las clases usar *
from PersonaEncapsulamiento import PersonaEncapsulamiento


if __name__ == '__main__':
    print('Object created'.center(50,'-'))
    person1 = PersonaEncapsulamiento('Pedro', 'Sanchez', 25)
    person1.show_details()
    print(__name__)

    print('Object deleted'.center(50,'-'))
    del person1

# Cuando trabajamos en POO en python creamos objetos y para eliminarlos, por una cuestión de liberar recursos podemos eliminarlo, llamado
# metodo destructor pero también lo hace el garbage collector en forma automatica