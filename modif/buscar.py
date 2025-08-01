from utils.corefiles import read_data, write_data
from utils.validatedata import validate_string 
from utils.screencontrollers import clear_screen, pause_screen
from utils. id import generate_id 
from tabulate import tabulate
import main_menu as main_menu 
FILENAME = 'coleccion.json'

def menu_buscar():
    data = read_data(FILENAME) 
    clear_screen()
    print("="*30)
    print("Buscar elementos")
    print("="*30)
    print("¿como decea buscar?")
    print("1. buscar por titulo")
    print("2. buscar por autor/artista/director")
    print("3. buscar por genero")
    print("4. buscar por identificador unico")
    print("5. Regresar al menú principal")
    print("="*30)

    opcion = input("Seleccione una opción: ")
    if opcion == '1':
        titulo = validate_string("Ingrese el título a buscar: ")
        resultados = buscar_titulos(data.get("peliculas", []), titulo) + \
                    buscar_titulos(data.get("libros", []), titulo) + \
                    buscar_titulos(data.get("musica", []), titulo)
        mostrar_resultados(resultados, titulo)
    elif opcion == '2':
        autor = validate_string("Ingrese el autor a buscar: ")
        resultados = buscar_autor(data.get("peliculas", []), autor) + \
                    buscar_autor(data.get("libros", []), autor) + \
                    buscar_autor(data.get("musica", []), autor)
        mostrar_resultados(resultados, autor)
    elif opcion == '3':
        genero = validate_string("Ingrese el género a buscar: ")
        resultados = buscar_genero(data.get("peliculas", []), genero) + \
                    buscar_genero(data.get("libros", []), genero) + \
                    buscar_genero(data.get("musica", []), genero)
        mostrar_resultados(resultados, genero)
    elif opcion == '4':
        identificador = validate_string("Ingrese el identificador único a buscar: ")
        resultados = buscar_identificador(data.get("peliculas", []), identificador) + \
                    buscar_identificador(data.get("libros", []), identificador) + \
                    buscar_identificador(data.get("musica", []), identificador)
        mostrar_resultados(resultados, identificador)
    elif opcion == '5':
        print("Regresando al menú principal...")
        main_menu.menu_principal()
    else:
        print("Opción no válida, intente de nuevo.")
        input("Presione Enter para continuar...")

def mostrar_resultados(resultados, criterio):
    if resultados:
        print(f"Resultados para '{criterio}':")
        print(tabulate(resultados, headers="keys", tablefmt="grid"))
    else:
        print(f"No se encontraron resultados para '{criterio}'.")
    pause_screen()
def buscar_titulos(lista, titulo):
    return [item for item in lista if item.get("titulo", "").lower() == titulo.lower()]     
def buscar_genero(lista, genero):
    return [item for item in lista if item.get("genero", "").lower() == genero.lower()]
def buscar_autor(lista, autor):
    return [item for item in lista if item.get("autor", "").lower() == autor.lower() or 
            item.get("artista", "").lower() == autor.lower() or 
            item.get("director", "").lower() == autor.lower()]
def buscar_identificador(lista, identificador):
    return [item for item in lista if item.get("identificador", "").lower() == identificador.lower()]