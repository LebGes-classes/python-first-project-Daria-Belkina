import os
import platform


def clear():
    """Функция, которая очищает консоль."""

    if platform.system() == 'Linux':
        os.system('clear')

    elif platform.system() == 'Windows':
        os.system('cls')