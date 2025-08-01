from utils.corefiles import read_data, write_data
from utils.validatedata import validate_string 
from utils.screencontrollers import clear_screen, pause_screen
import os 

BASE_PATH = 'data/'
COLECCION_ACTUAL_FILENAME = 'coleccion_actual.json'

coleccion_actual = {}  

def menu_coleccion(): 
    while True:
        clear_screen()
        print("=== Menú de Colección ===")
        print("1. Guardar la Colección Actual")
        print("2. Nombrar y Guardar la Colección")
        print("3. Cargar una Colección Guardada")
        print("4. Ver Colecciones Guardadas")
        print("5. Regresar al Menú Principal")
        print("==========================")

        opcion = input("Selecciona una opción")

        if opcion == "1":
            guardar_coleccion_actual()
        elif opcion == "2":
            nombrar_y_guardar_coleccion()
        elif opcion == "3":
            cargar_coleccion_guardada()
        elif opcion == "4":
            ver_colecciones_guardadas()
        elif opcion == "5":
            print(" Regresando al menú principal...")
            break

        pause_screen()
        
def guardar_coleccion_actual():
    write_data(COLECCION_ACTUAL_FILENAME, coleccion_actual)
    print("Colección actual guardada como 'coleccion_actual.json'.")

def nombrar_y_guardar_coleccion():
    nombre = validate_string(" Nombre para la nueva colección: ")
    filename = f"{nombre}.json"
    write_data(filename, coleccion_actual)
    print(f" Colección guardada como '{filename}'.")

def cargar_coleccion_guardada():
    ver_colecciones_guardadas()
    nombre = validate_string(" Ingrese el nombre de la colección a cargar (sin '.json'): ")
    filename = f"{nombre}.json"
    data = read_data(filename)
    if not data:
        print(" Colección vacía o no encontrada.")
        return
    coleccion_actual.clear()
    coleccion_actual.update(data)
    print(f" Colección '{filename}' cargada correctamente.")


def ver_colecciones_guardadas():
    try:
        archivos = [f for f in os.listdir(BASE_PATH) if f.endswith('.json')]
        if not archivos:
            print(" No hay colecciones guardadas.")
        else:
            print(" Colecciones disponibles:")
            for i, archivo in enumerate(archivos, 1):
                print(f"{i}. {archivo}")
    except FileNotFoundError:
        print("Carpeta de datos no encontrada.")