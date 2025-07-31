from utils.corefiles import read_data, write_data
from utils.screencontrollers import clear_screen, pause_screen
import main_menu as main_menu
from tabulate import tabulate

FILENAME = 'coleccion.json'

def menu_ver():
    clear_screen()
    print("="*30)
    print("¿que categoria desea ver?")
    print("="*30)
    print("1. Películas")
    print("2. Libros")
    print("3. Musica") 
    print("4. Regresar al menú principal")
    print("="*30)
    
    opcion = input("Seleccione una opción: ")
    clear_screen()
    if opcion == '1':
        ver_peliculas(peliculas_data=read_data(FILENAME))
    elif opcion == '2':
        ver_libros(libros_data=read_data(FILENAME))
    elif opcion == '3':
        ver_musica(musica_data=read_data(FILENAME)  )
    elif opcion == '4':
        print("Regresando al menú principal...")
        print(main_menu.menu_principal())
    else:
        print("Opción no válida, intente de nuevo.")
        input("Presione Enter para continuar...")

def ver_peliculas(peliculas_data):
    clear_screen()
    peliculas_data = read_data(FILENAME)
    filtrados=[pelicula for pelicula in peliculas_data.get("peliculas", []) if pelicula]
    print(tabulate(filtrados, headers="keys", tablefmt="grid"))
    pause_screen()
    input("Presione Enter para continuar...")

def ver_libros(libros_data):
    clear_screen()
    libros_data = read_data(FILENAME)
    filtrados=[libro for libro in libros_data.get("libros", []) if libro]
    print(tabulate(filtrados, headers="keys", tablefmt="grid"))
    pause_screen()
    input("Presione Enter para continuar...")

def ver_musica(musica_data):
    clear_screen()
    musica_data = read_data(FILENAME)
    filtrados=[musica for musica in musica_data.get("musica", []) if musica]
    print(tabulate(filtrados, headers="keys", tablefmt="grid"))
    pause_screen()
    input("Presione Enter para continuar...")
