from utils.corefiles import read_data, write_data
from utils.validatedata import validate_string 
from utils.screencontrollers import clear_screen, pause_screen
from modif import buscar 
from tabulate import tabulate
import main_menu as main_menu 

FILENAME = 'coleccion.json'

def menu_eliminar():
    data = read_data(FILENAME) 
    clear_screen()
    print("="*30)
    print("Eliminar elementos")
    print("="*30)
    print("¿Cómo desea eliminar?")
    print("1. Eliminar por título")
    print("2. Eliminar por identificador único")
    print("3. Regresar al menú principal")
    print("="*30)
    
    opcion = input("Seleccione una opción: ")
    if opcion == '1':
        titulo = validate_string("Ingrese el título a eliminar: ")
        resultados = buscar.buscar_titulos(data.get("peliculas", []), titulo) + \
                     buscar.buscar_titulos(data.get("libros", []), titulo) + \
                     buscar.buscar_titulos(data.get("musica", []), titulo)
        eliminar_resultados(data, resultados, titulo)
    elif opcion == '2':
        identificador = validate_string("Ingrese el identificador único a eliminar: ")
        resultados = buscar.buscar_identificador(data.get("peliculas", []), identificador) + \
                     buscar.buscar_identificador(data.get("libros", []), identificador) + \
                     buscar.buscar_identificador(data.get("musica", []), identificador)
        eliminar_resultados(data, resultados, identificador)
    elif opcion == '3':
        print("Regresando al menú principal...")
        pause_screen()
        main_menu.menu_principal()
    else:
        print("Opción no válida.")
    pause_screen()

def eliminar_resultados(data, resultados, criterio):
    if resultados:
        print(f"Resultados para '{criterio}':")
        print(tabulate(resultados, headers="keys", tablefmt="grid"))

        confirmacion = input("¿Está seguro de que desea eliminar estos elementos? (s/n): ")
        if confirmacion.lower() == 's':
            for item in resultados:
                for categoria in ["peliculas", "libros", "musica"]:
                    if item in data.get(categoria, []):
                        data[categoria].remove(item)
            write_data(FILENAME, data)
            print("Elementos eliminados correctamente.")
        else:
            print("Eliminación cancelada.")
    else:
        print(f"No se encontraron resultados para '{criterio}'.")

def buscar_identificador(data, identificador):
    return [item for item in data if item.get('id', '') == identificador]