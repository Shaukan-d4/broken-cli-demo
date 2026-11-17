import tomllib   #BUG 1: ImportError at Python 3.10
import requests #BUG 3: ModuleNotFoundError for user

def start():
    # BUG 2: Windows gives error while reading UTF-8 symbols
    with open("data.txt") as f:
        print(f.read())
