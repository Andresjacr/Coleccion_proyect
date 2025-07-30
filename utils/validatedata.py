def validate_string(prompt: str) -> str:
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Error: La entrada no puede estar vacía.")

def validate_int(prompt: str) -> int:
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Error: Por favor, ingrese un número entero válido.")

def validate_option(prompt: str, valid_options: list) -> str:
    while True:
        value = input(prompt).strip().lower()
        if value in valid_options:
            return value
        print(f"Error: Opción no válida. Opciones permitidas: {', '.join(valid_options)}") 