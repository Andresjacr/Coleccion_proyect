import os
import platform

def clear_screen():
    try:
        command = 'cls' if platform.system() == 'Windows' else 'clear'
        
        if os.system(command) != 0:
            print('\n' * 100)
            
    except Exception:
        print('\n' * 100)

def pause_screen():

    input("Presione Enter para continuar...")