from utils.corefiles import read_data, write_data
from utils.validatedata import validate_string 
from utils.screencontrollers import clear_screen, pause_screen
from utils.id import generate_id
import main_menu as main_menu 
FILENAME = 'coleccion.json'

def menu_anadir():
    clear_screen()
    print("="*30)
    print("Añadir un nuevo elemento")
    print("="*30)
    print("¿Qué tipo de elemento desea añadir?")
    print("1. Película")
    print("2. Libro")
    print("3. Música")
    print("4. Regresar al menú principal")
    print("="*30)

    opcion = input("Seleccione una opción: ")
    if opcion == '1':
        añadir_pelicula()
    elif opcion == '2':
        añadir_libro()
    elif opcion == '3':
        añadir_musica()
    elif opcion == '4':
        print("Regresando al menú principal...")
        print(main_menu.menu_principal())
    else:
        print("Opción no válida, intente de nuevo.")
        input("Presione Enter para continuar...")
        
def añadir_pelicula():
    clear_screen()
    
    peliculas_data = read_data(FILENAME)
    pelicula_id = generate_id(peliculas_data)

    titulo = validate_string("Ingrese el título de la película: ")
    director = validate_string("Ingrese el director de la película: ")
    genero = validate_string("Ingrese el género de la película: ")
    valoracion = validate_string("Ingrese la valoración de la película: ")

    nueva_pelicula = {
            "titulo": titulo,
            "director": director,
            "genero": genero,
        "valoracion": valoracion,
        "id": pelicula_id
    }
    peliculas_data.setdefault("peliculas", []).append(nueva_pelicula)
    write_data(FILENAME, peliculas_data)    
    print(f"Película '{titulo}' añadida correctamente.")
    pause_screen()
    
def añadir_libro():
    clear_screen()
    
    libros_data = read_data(FILENAME)
    libro_id = generate_id(libros_data)

    titulo = validate_string("Ingrese el título del libro: ")
    autor = validate_string("Ingrese el autor del libro: ")
    genero = validate_string("Ingrese el género del libro: ")
    valoracion = validate_string("Ingrese la valoración del libro: ")
    nuevo_libro = {
        "titulo": titulo,
        "autor": autor,
        "genero": genero,
        "valoracion": valoracion,
        "id": libro_id
    }
    libros_data.setdefault("libros", []).append(nuevo_libro)
    write_data(FILENAME, libros_data)
    print(f"Libro '{titulo}' añadido correctamente.")
    pause_screen()
    
def añadir_musica():
    clear_screen()
    musica_data = read_data(FILENAME)
    musica_id = generate_id(musica_data)
    titulo = validate_string("Ingrese el título de la música: ")
    artista = validate_string("Ingrese el artista de la música: ")
    genero = validate_string("Ingrese el género de la música: ")
    valoracion = validate_string("Ingrese la valoración de la música: ")
    nueva_musica = {
        "titulo": titulo,
        "artista": artista,
        "genero": genero,
        "valoracion": valoracion,
        "id": musica_id
    }
    musica_data.setdefault("musica", []).append(nueva_musica)
    write_data(FILENAME, musica_data)
    print(f"Música '{titulo}' añadida correctamente.")
    pause_screen()