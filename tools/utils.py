from os import PathLike
from pathlib import Path

def check(condition:bool, message:str) -> bool:
    if not condition:
        print(f'ERROR: {message}')
        return False
    return True