import json
import os

BASE_PATH = 'data/'

def check_file(filename: str):
    if not os.path.exists(BASE_PATH):
        os.makedirs(BASE_PATH)
    
    filepath = os.path.join(BASE_PATH, filename)
    if not os.path.isfile(filepath):
        try:
            with open(filepath, 'w') as file:
                json.dump({}, file, indent=4)
        except Exception as e:
            print(f"Error al crear el archivo {filepath}: {e}")

def read_data(filename: str) -> dict:
    check_file(filename)
    filepath = os.path.join(BASE_PATH, filename)
    try:
        with open(filepath, 'r') as file:
            return json.load(file)
    except (json.JSONDecodeError, IOError):
        return {}
    except Exception as e:
        print(f"Error al leer el archivo {filepath}: {e}")
        return {}

def write_data(filename: str, data: dict):
    """
    Escribe datos en un archivo JSON.
    """
    check_file(filename)
    filepath = os.path.join(BASE_PATH, filename)
    try:
        with open(filepath, 'w') as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        print(f"Error al escribir en el archivo {filepath}: {e}")