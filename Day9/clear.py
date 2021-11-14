import os
from time import sleep

def clear_screen():
    # for macos and linux
    if os.name == 'posix':
        _ = os.system('clear')
    # for windows
    else:
        _ = os.system('cls')

