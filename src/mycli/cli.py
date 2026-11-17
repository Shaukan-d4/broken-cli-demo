"""import sys
import requests

# Фикс Бага 1: fallback на tomli для Python 3.10
if sys.version_info >= (3, 11):
    import tomllib
else:
    import tomli as tomllib


# Фикс Бага 4: функция называется main, как указано в pyproject.toml
def main():
    if "--help" in sys.argv or "-h" in sys.argv:
        print("Usage: mycli [options]")
        return

    # Фикс Бага 2: явная кодировка utf-8 для корректной работы на Windows
    try:
        with open("data.txt", encoding="utf-8") as f:
            print(f.read())
    except FileNotFoundError:
        print("Ready! (data.txt not found, default mode)")
"""
import sys


def main():
    if "--help" in sys.argv or "-h" in sys.argv:
        print("Usage: mycli [options]")
        return

    try:
        with open("data.txt", encoding="utf-8") as f:
            print(f.read())
    except FileNotFoundError:
        print("Ready! (data.txt not found, default mode)")
