# un archivo o modulo puede tener mas de una clase - para traer todas las clases usar *
from PersonaEncapsulamiento import PersonaEncapsulamiento


if __name__ == '__main__':
    person1 = PersonaEncapsulamiento('Pedro', 'Sanchez', 25)
    person1.show_details()

    print(__name__)