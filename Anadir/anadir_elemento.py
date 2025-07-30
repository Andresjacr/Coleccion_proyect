from utils.corefiles import  write_Data 
import os

write_Data= {
    'peliculas.json': [],
    'libros.json': [],
    'musica.json': []
}

def menu_anadir():
    os.system('cls' if os.name == 'nt' else 'clear')
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
        return (menu_anadir)
    else:
        print("Opción no válida, intente de nuevo.")
        input("Presione Enter para continuar...")
        
def añadir_pelicula():
    titulo = input("Ingrese el título de la película: ")
    autor = input("Ingrese el autor de la película: ")
    genero = input("Ingrese el género de la película: ")
    valoracion = input("Ingrese la valoración de la película: ")
    with Data('peliculas.json', 'a') as Data:
        Data.write(f"{titulo},{autor},{genero},{valoracion}\n")
    print(f"Película '{titulo}' añadida correctamente.")
    
  
def añadir_libro():
    titulo = input("Ingrese el título del libro: ")
    autor = input("Ingrese el autor del libro: ")
    genero = input("Ingrese el género del libro: ")
    valoracion = input("Ingrese la valoración del libro: ")
    with Data('libros.json', 'a') as Data:
        Data.write(f"{titulo},{autor},{genero},{valoracion}\n")
    print(f"Libro '{titulo}' añadido correctamente.")
    
def añadir_musica():
    titulo = input("Ingrese el título de la música: ")
    autor = input("Ingrese el autor de la música: ")
    genero = input("Ingrese el género de la música: ")
    valoracion = input("Ingrese la valoración de la música: ")
    with Data('musica.json', 'a') as Data:
        Data.write(f"{titulo},{autor},{genero},{valoracion}\n")
    print(f"Música '{titulo}' añadida correctamente.")
    