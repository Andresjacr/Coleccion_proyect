import json
import os   

def generate_id(peliculas_data: dict) -> str:
    max_num = 0
    for key in peliculas_data.keys():
        if key.startswith('pelicula'):
            try:
                num = int(key[8:]) 
                if num > max_num:
                    max_num = num
            except (ValueError, IndexError):
                continue
    new_num = max_num + 1
    return f"pelicula{new_num:04d}"

def generate_id(libros_data: dict) -> str:
    max_num = 0
    for key in libros_data.keys():
        if key.startswith('libro'):
            try:
                num = int(key[5:]) 
                if num > max_num:
                    max_num = num
            except (ValueError, IndexError):
                continue
    new_num = max_num + 1
    return f"libro{new_num:04d}"

def generate_id(musica_data: dict) -> str:
    max_num = 0
    for key in musica_data.keys():
        if key.startswith('musica'):
            try:
                num = int(key[6:]) 
                if num > max_num:
                    max_num = num
            except (ValueError, IndexError):
                continue
    new_num = max_num + 1
    return f"musica{new_num:04d}"
