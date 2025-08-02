from utils.corefiles import read_data
from utils.validatedata import validate_string 
from utils.screencontrollers import clear_screen, pause_screen
from tabulate import tabulate 

FILENAME = 'coleccion.json'

def menu_categorias():
    """Menú principal para ver elementos por categoría"""
    clear_screen()
    print("="*40)
    print("Ver elementos por categoría")
    print("="*40)
    print("¿Qué categoría desea explorar?")
    print("1. Películas por género")
    print("2. Libros por género")
    print("3. Música por género")
    print("4. Regresar al menú principal")
    print("="*40)

    opcion = input("Seleccione una opción: ")
    if opcion == '1':
        mostrar_generos_peliculas()
    elif opcion == '2':
        mostrar_generos_libros()
    elif opcion == '3':
        mostrar_generos_musica()
    elif opcion == '4':
        print("Regresando al menú principal...")
        return
    else:
        print("Opción no válida, intente de nuevo.")
        pause_screen()
        menu_categorias()

def mostrar_generos_peliculas():
    """Muestra los géneros disponibles de películas y permite seleccionar uno"""
    data = read_data(FILENAME)
    peliculas = data.get("peliculas", [])
    
    if not peliculas:
        clear_screen()
        print("No hay películas en la colección.")
        pause_screen()
        return
    
    generos = list(set(pelicula.get("genero", "").lower() for pelicula in peliculas if pelicula.get("genero")))
    generos.sort()
    
    clear_screen()
    print("="*40)
    print("Géneros de películas disponibles:")
    print("="*40)
    
    if not generos:
        print("No se encontraron géneros definidos.")
        pause_screen()
        return
    
    for i, genero in enumerate(generos, 1):
        print(f"{i}. {genero.title()}")
    print(f"{len(generos) + 1}. Ver todas las películas")
    print(f"{len(generos) + 2}. Regresar")
    print("="*40)
    
    try:
        opcion = int(input("Seleccione un género: "))
        if 1 <= opcion <= len(generos):
            genero_seleccionado = generos[opcion - 1]
            mostrar_peliculas_por_genero(peliculas, genero_seleccionado)
        elif opcion == len(generos) + 1:
            mostrar_todas_peliculas(peliculas)
        elif opcion == len(generos) + 2:
            return
        else:
            print("Opción no válida.")
            pause_screen()
    except ValueError:
        print("Por favor, ingrese un número válido.")
        pause_screen()

def mostrar_generos_libros():
    data = read_data(FILENAME)
    libros = data.get("libros", [])
    
    if not libros:
        clear_screen()
        print("No hay libros en la colección.")
        pause_screen()
        return
    
    generos = list(set(libro.get("genero", "").lower() for libro in libros if libro.get("genero")))
    generos.sort()
    
    clear_screen()
    print("="*40)
    print("Géneros de libros disponibles:")
    print("="*40)
    
    if not generos:
        print("No se encontraron géneros definidos.")
        pause_screen()
        return
    
    for i, genero in enumerate(generos, 1):
        print(f"{i}. {genero.title()}")
    print(f"{len(generos) + 1}. Ver todos los libros")
    print(f"{len(generos) + 2}. Regresar")
    print("="*40)
    
    try:
        opcion = int(input("Seleccione un género: "))
        if 1 <= opcion <= len(generos):
            genero_seleccionado = generos[opcion - 1]
            mostrar_libros_por_genero(libros, genero_seleccionado)
        elif opcion == len(generos) + 1:
            mostrar_todos_libros(libros)
        elif opcion == len(generos) + 2:
            return
        else:
            print("Opción no válida.")
            pause_screen()
    except ValueError:
        print("Por favor, ingrese un número válido.")
        pause_screen()

def mostrar_generos_musica():
    data = read_data(FILENAME)
    musica = data.get("musica", [])
    
    if not musica:
        clear_screen()
        print("No hay música en la colección.")
        pause_screen()
        return
    
    generos = list(set(cancion.get("genero", "").lower() for cancion in musica if cancion.get("genero")))
    generos.sort()
    
    clear_screen()
    print("="*40)
    print("Géneros de música disponibles:")
    print("="*40)
    
    if not generos:
        print("No se encontraron géneros definidos.")
        pause_screen()
        return
    
    for i, genero in enumerate(generos, 1):
        print(f"{i}. {genero.title()}")
    print(f"{len(generos) + 1}. Ver toda la música")
    print(f"{len(generos) + 2}. Regresar")
    print("="*40)
    
    try:
        opcion = int(input("Seleccione un género: "))
        if 1 <= opcion <= len(generos):
            genero_seleccionado = generos[opcion - 1]
            mostrar_musica_por_genero(musica, genero_seleccionado)
        elif opcion == len(generos) + 1:
            mostrar_toda_musica(musica)
        elif opcion == len(generos) + 2:
            return
        else:
            print("Opción no válida.")
            pause_screen()
    except ValueError:
        print("Por favor, ingrese un número válido.")
        pause_screen()

def mostrar_peliculas_por_genero(peliculas, genero):
    peliculas_filtradas = [p for p in peliculas if p.get("genero", "").lower() == genero.lower()]
    
    clear_screen()
    print("="*50)
    print(f"Películas del género: {genero.title()}")
    print("="*50)
    
    if peliculas_filtradas:
        print(tabulate(peliculas_filtradas, headers="keys", tablefmt="grid"))
        print(f"\nTotal de películas encontradas: {len(peliculas_filtradas)}")
    else:
        print(f"No se encontraron películas del género '{genero}'.")
    
    pause_screen()

def mostrar_libros_por_genero(libros, genero):
    libros_filtrados = [l for l in libros if l.get("genero", "").lower() == genero.lower()]
    
    clear_screen()
    print("="*50)
    print(f"Libros del género: {genero.title()}")
    print("="*50)
    
    if libros_filtrados:
        print(tabulate(libros_filtrados, headers="keys", tablefmt="grid"))
        print(f"\nTotal de libros encontrados: {len(libros_filtrados)}")
    else:
        print(f"No se encontraron libros del género '{genero}'.")
    
    pause_screen()

def mostrar_musica_por_genero(musica, genero):
    musica_filtrada = [m for m in musica if m.get("genero", "").lower() == genero.lower()]
    
    clear_screen()
    print("="*50)
    print(f"Música del género: {genero.title()}")
    print("="*50)
    
    if musica_filtrada:
        print(tabulate(musica_filtrada, headers="keys", tablefmt="grid"))
        print(f"\nTotal de canciones encontradas: {len(musica_filtrada)}")
    else:
        print(f"No se encontró música del género '{genero}'.")
    
    pause_screen()

def mostrar_todas_peliculas(peliculas):
    """Muestra todas las películas"""
    clear_screen()
    print("="*50)
    print("Todas las películas")
    print("="*50)
    
    if peliculas:
        print(tabulate(peliculas, headers="keys", tablefmt="grid"))
        print(f"\nTotal de películas: {len(peliculas)}")
    else:
        print("No hay películas en la colección.")
    
    pause_screen()

def mostrar_todos_libros(libros):
    """Muestra todos los libros"""
    clear_screen()
    print("="*50)
    print("Todos los libros")
    print("="*50)
    
    if libros:
        print(tabulate(libros, headers="keys", tablefmt="grid"))
        print(f"\nTotal de libros: {len(libros)}")
    else:
        print("No hay libros en la colección.")
    
    pause_screen()

def mostrar_toda_musica(musica):
    """Muestra toda la música"""
    clear_screen()
    print("="*50)
    print("Toda la música")
    print("="*50)
    
    if musica:
        print(tabulate(musica, headers="keys", tablefmt="grid"))
        print(f"\nTotal de canciones: {len(musica)}")
    else:
        print("No hay música en la colección.")
    
    pause_screen()