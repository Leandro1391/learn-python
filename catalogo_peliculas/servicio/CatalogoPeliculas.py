from dominio.Pelicula import Pelicula
import os

# el with es un Contexto Manager, se encarga de abrir y cerrar el arhicvo automaticamente
# with open('test.txt', 'r', encoding='utf8') as file:
#     print(file.read())

class CatalogoPeliculas:

    ruta_archivo: str = 'peliculas.txt'

    def __init__(self):
        pass
    
    @classmethod
    def agregar_pelicula(cls, unaPelicula: Pelicula):
        with open(cls.ruta_archivo, 'a', encoding='utf8') as file:
            file.write(f'{unaPelicula.name}\n')
    @classmethod
    def listar_peliculas(cls):
        with open(cls.ruta_archivo, 'r', encoding='utf8') as file:
            print(file.read())
            
    @classmethod
    def eliminar(cls):
        if os.path.exists(cls.ruta_archivo):
            os.remove(cls.ruta_archivo)
        else:
            print("The file does not exist")

            

if __name__ == '__main__':
    unCatalogoPeli = CatalogoPeliculas()
    unaPeli = Pelicula('Silvestre')
    segundaPeli = Pelicula('Linterna verde')
    unCatalogoPeli.agregar_pelicula(unaPeli)
    unCatalogoPeli.agregar_pelicula(segundaPeli)
    unCatalogoPeli.listar_peliculas()
    # unCatalogoPeli.eliminar()