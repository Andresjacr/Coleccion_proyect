from utils.corefiles import read_data, write_data
from utils.validatedata import validate_string 
from utils.screencontrollers import clear_screen, pause_screen
from modif import buscar 
from tabulate import tabulate
import main_menu as main_menu 

FILENAME = 'coleccion.json'

def menu_editar():
    while True:
        clear_screen()
        print("===========================================")
        print("        Editar un Elemento")
        print("===========================================")
        print("1. Buscar y editar elemento")
        print("2. Regresar al Menú Principal")
        print("===========================================")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            buscar_y_editar()
        elif opcion == '2':
            print("\nRegresando al Menú Principal...")
            break
        else:
            print("\nOpción no válida. Por favor, selecciona un número del 1 al 2.")
            pause_screen()

def buscar_y_editar():
    data = read_data(FILENAME)
    clear_screen()
    print("="*40)
    print("Buscar elemento para editar")
    print("="*40)
    print("¿Cómo desea buscar el elemento?")
    print("1. Buscar por título")
    print("2. Buscar por identificador único")
    print("3. Regresar")
    print("="*40)

    opcion = input("Seleccione una opción: ")
    
    if opcion == '1':
        titulo = validate_string("Ingrese el título a buscar: ")
        resultados = buscar_por_titulo_todas_categorias(data, titulo)
        if resultados:
            seleccionar_y_editar(data, resultados, "título", titulo)
        else:
            print(f"No se encontraron elementos con el título '{titulo}'.")
            pause_screen()
            
    elif opcion == '2':
        identificador = validate_string("Ingrese el identificador único: ")
        resultados = buscar_por_id_todas_categorias(data, identificador)
        if resultados:
            seleccionar_y_editar(data, resultados, "identificador", identificador)
        else:
            print(f"No se encontró elemento con el identificador '{identificador}'.")
            pause_screen()
            
    elif opcion == '3':
        return
    else:
        print("Opción no válida.")
        pause_screen()

def buscar_por_titulo_todas_categorias(data, titulo):
    resultados = []
    for categoria in ["peliculas", "libros", "musica"]:
        items = data.get(categoria, [])
        for item in items:
            if item.get("titulo", "").lower() == titulo.lower():
                item_con_categoria = item.copy()
                item_con_categoria["categoria"] = categoria
                resultados.append(item_con_categoria)
    return resultados

def buscar_por_id_todas_categorias(data, identificador):
    resultados = []
    for categoria in ["peliculas", "libros", "musica"]:
        items = data.get(categoria, [])
        for item in items:
            if item.get("id", "") == identificador:
                item_con_categoria = item.copy()
                item_con_categoria["categoria"] = categoria
                resultados.append(item_con_categoria)
    return resultados

def seleccionar_y_editar(data, resultados, tipo_busqueda, criterio):
    clear_screen()
    print(f"Resultados encontrados para {tipo_busqueda} '{criterio}':")
    print()
    
    # Mostrar resultados sin la columna categoria
    resultados_mostrar = []
    for i, item in enumerate(resultados, 1):
        item_mostrar = {k: v for k, v in item.items() if k != "categoria"}
        item_mostrar["#"] = i
        resultados_mostrar.append(item_mostrar)
    
    print(tabulate(resultados_mostrar, headers="keys", tablefmt="grid"))
    print()
    
    if len(resultados) == 1:
        print("Solo hay un elemento. Se editará automáticamente.")
        editar_elemento(data, resultados[0])
    else:
        while True:
            try:
                seleccion = int(input(f"Seleccione el número del elemento a editar (1-{len(resultados)}): "))
                if 1 <= seleccion <= len(resultados):
                    editar_elemento(data, resultados[seleccion - 1])
                    break
                else:
                    print(f"Por favor, ingrese un número entre 1 y {len(resultados)}.")
            except ValueError:
                print("Por favor, ingrese un número válido.")

def editar_elemento(data, elemento):
    categoria = elemento["categoria"]
    elemento_original = {k: v for k, v in elemento.items() if k != "categoria"}
    
    while True:
        clear_screen()
        print("="*50)
        print("        Editar Elemento")
        print("="*50)
        print("Elemento actual:")
        print(tabulate([elemento_original], headers="keys", tablefmt="grid"))
        print()
        print("¿Qué campo desea editar?")
        print("1. Título")
        
        if categoria == "peliculas":
            print("2. Director")
        elif categoria == "libros":
            print("2. Autor")
        elif categoria == "musica":
            print("2. Artista")
            
        print("3. Género")
        print("4. Valoración")
        print("5. Guardar cambios y salir")
        print("6. Cancelar (sin guardar)")
        print("="*50)
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            nuevo_titulo = validate_string("Ingrese el nuevo título: ")
            elemento_original["titulo"] = nuevo_titulo
            print(f"Título actualizado a: '{nuevo_titulo}'")
            pause_screen()
            
        elif opcion == '2':
            if categoria == "peliculas":
                nuevo_valor = validate_string("Ingrese el nuevo director: ")
                elemento_original["director"] = nuevo_valor
                print(f"Director actualizado a: '{nuevo_valor}'")
            elif categoria == "libros":
                nuevo_valor = validate_string("Ingrese el nuevo autor: ")
                elemento_original["autor"] = nuevo_valor
                print(f"Autor actualizado a: '{nuevo_valor}'")
            elif categoria == "musica":
                nuevo_valor = validate_string("Ingrese el nuevo artista: ")
                elemento_original["artista"] = nuevo_valor
                print(f"Artista actualizado a: '{nuevo_valor}'")
            pause_screen()
            
        elif opcion == '3':
            nuevo_genero = validate_string("Ingrese el nuevo género: ")
            elemento_original["genero"] = nuevo_genero
            print(f"Género actualizado a: '{nuevo_genero}'")
            pause_screen()
            
        elif opcion == '4':
            nueva_valoracion = validate_string("Ingrese la nueva valoración: ")
            elemento_original["valoracion"] = nueva_valoracion
            print(f"Valoración actualizada a: '{nueva_valoracion}'")
            pause_screen()
            
        elif opcion == '5':
            
            actualizar_elemento_en_datos(data, categoria, elemento["id"], elemento_original)
            write_data(FILENAME, data)
            print("¡Cambios guardados exitosamente!")
            pause_screen()
            break
            
        elif opcion == '6':
            print("Edición cancelada. No se guardaron los cambios.")
            pause_screen()
            break
            
        else:
            print("Opción no válida. Por favor, seleccione un número del 1 al 6.")
            pause_screen()

def actualizar_elemento_en_datos(data, categoria, elemento_id, elemento_actualizado):
    """Actualiza el elemento en la estructura de datos"""
    items = data.get(categoria, [])
    for i, item in enumerate(items):
        if item.get("id") == elemento_id:
            data[categoria][i] = elemento_actualizado
            break