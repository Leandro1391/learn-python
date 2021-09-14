from dominio.Pelicula import Pelicula
from servicio.CatalogoPeliculas import CatalogoPeliculas

unCatalogoPeliculas = CatalogoPeliculas()
while True:
    try:
        option = int(input("""Menu de Opciones:
        1. Agregar pelicula
        2. Listar peliculas
        3. Eliminar catálogo de peliculas
        4. Salir
        Opcion elegida: """))
        if option == 1:
            name = str(input(f"Ingrese nombre de la pelicula: "))
            unaPelicula = Pelicula(name)
            unCatalogoPeliculas.agregar_pelicula(unaPelicula)
        elif option == 2:
            unCatalogoPeliculas.listar_peliculas()
        elif option == 3:
            unCatalogoPeliculas.eliminar()
        elif option == 4:
            break
        else:
            "Por favor ingrese un numero del 1 al 4\n"
    except Exception as e:
        print(f'Exception - Error handled: {e}, {type(e)}')
    