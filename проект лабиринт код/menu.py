from clearing import clear


class Menu:
    """Класс для работы с меню."""

    @staticmethod
    def print_main_menu() -> None:
        """Функция, которая печатает главное меню."""

        clear()
        print('-----МЕНЮ-----')
        print('1) Выбор уровня')
        print('2) Выход')

    @staticmethod
    def show_pause_menu() -> str:
        """Функция, которая отображает меню паузы.

        Returns:
            choice: Выбор пользователя.
        """

        print("\n[Пауза]")
        print("1) Продолжить")
        print("2) В главное меню")

        choice = input("Выберите пункт 1 или 2: ")

        return choice
