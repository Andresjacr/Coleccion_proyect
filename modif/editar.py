from utils.corefiles import read_data, write_data
from utils.validatedata import validate_string 
from utils.screencontrollers import clear_screen, pause_screen
from modif import buscar 
from tabulate import tabulate
import main_menu as main_menu 

FILENAME = 'coleccion.json'

def menu_editar():
    print("===========================================")
    print("        Editar un Elemento")
    print("===========================================")
    print("¿Qué tipo de cambio deseas realizar?")
    print("1. Editar Título")
    print("2. Editar Autor/Director/Artista")
    print("3. Editar Género")
    print("4. Editar Valoración")
    print("5. Regresar al Menú Principal")
    print("===========================================")
    
    opcion = input("seleccione una opcion...")
    if opcion == '1':
        print("\n--- Has seleccionado: Editar Título ---")
        nuevo_titulo = input("Introduce el nuevo título: ")
        print(f"¡El título ha sido actualizado a '{nuevo_titulo}'!")
        input("\nPresiona Enter para continuar...")
        
    elif opcion == '2':
        print("\n--- Has seleccionado: Editar Autor/Director/Artista ---")
        nuevo_artista = input("Introduce el nuevo nombre: ")
        print(f"¡El autor/director/artista ha sido actualizado a '{nuevo_artista}'!")
        input("\nPresiona Enter para continuar...")

    elif opcion == '3':
        print("\n--- Has seleccionado: Editar Género ---")
        nuevo_genero = input("Introduce el nuevo género: ")
        print(f"¡El género ha sido actualizado a '{nuevo_genero}'!")
        input("\nPresiona Enter para continuar...")

    elif opcion == '4':
        print("\n--- Has seleccionado: Editar Valoración ---")
        nueva_valoracion = input("Introduce la nueva valoración (ej. 1-5 estrellas): ")
        print(f"¡La valoración ha sido actualizada a '{nueva_valoracion}'!")
        input("\nPresiona Enter para continuar...")

    elif opcion == '5':
        print("\nRegresando al Menú Principal...")

    else:
            print("\nOpción no válida. Por favor, selecciona un número del 1 al 5.")
            input("\nPresiona Enter para continuar...")
