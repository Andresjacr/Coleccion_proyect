import sys 
from Anadir import anadir_elemento
from tablas_contenido import contenido 
from modif import buscar
from modif import eliminar 
from modif import colecciones
from modif import editar
from utils.screencontrollers import clear_screen, pause_screen

def menu_principal():
    clear_screen()
    print("="*30)
    print("Menu Principal")
    print("="*30) 
    print("1. añadir un nuevo elemento")
    print("2. ver elementos existentes")
    print("3. buscar un elemento")
    print("4. editar elementos")
    print("5. eliminar un elemento")
    print("6. ver elementos por categoria")
    print("7. guardar y cargar coleccion ")
    print("8. salir")
    print("="*30)

def main():
    while True:
        menu_principal()
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            anadir_elemento.menu_anadir()
        elif opcion == '2':
            contenido.menu_ver()  
        elif opcion == '3':
            buscar.menu_buscar()
        elif opcion == '4':
            editar.menu_editar
        elif opcion == '5':
            eliminar.menu_eliminar() 
        elif opcion == '6':
            pass
        elif opcion == '7':
            colecciones.menu_coleccion()
        elif opcion == '8':
            print("Saliendo del programa...")
            sys.exit()
            break
        else:
            print("Opción no válida, intente de nuevo.")
            input("Presione Enter para continuar...")

if __name__ == "__main__":
    main()