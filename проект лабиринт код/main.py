import time
from menu import Menu
from maze_game import MazeGame
from maze_generator import MazeGenerator
from clearing import clear


class Main:
    """Основной класс игры."""

    def run(self) -> None:
        """Функция для вывода меню, выбора и запуска уровня, завершения программы."""

        is_running = True

        while is_running:
            Menu.print_main_menu()

            choise = int(input('Введите пункт меню >>> '))

            if choise == 1:
                choise_level = int(input('Выберите уровень 1/2/3/4: '))

                if choise_level == 1:
                    self.play(1)

                elif choise_level == 2:
                    self.play(2)

                elif choise_level == 3:
                    self.play(3)

                elif choise_level == 4:
                    self.play(4)

                else:
                    input("Неверный уровень. Нажмите Enter и попробуйте еще раз.")

            elif choise == 2:
                is_running = False

            else:
                input("Неверный ввод. Нажмите Enter и попробуйте еще раз.")

    def play(self, chosen_level) -> None:
        """Игровой цикл для одного выбранного уровня.

        Args:
            chosen_level: Номер выбранного уровня.
        """

        level_sizes = [[15, 13], [17, 19], [21, 23], [23, 25]]
        width, height = level_sizes[chosen_level - 1]
        play_map = MazeGenerator(width, height)
        lab=play_map.generate_maze()
        start = (1, 1)
        exit_position = (height - 2, width - 2)
        maze = MazeGame(lab, start, exit_position)
        won = False
        start_time = time.time()

        while not won:
            clear()
            maze.render(chosen_level)

            if maze.is_winner():
                end_time = time.time()
                level_time = end_time - start_time

                print("\n✅ Поздравляю! Уровень пройден!")
                print(f"Время прохождения: {level_time:.2f} сек.")

                won = True

                input("\nНажмите Enter для возврата в меню")

                break

            action = input("\nХод: ")

            if action in ("w", "a", "s", "d"):
                maze.move(action)

            elif action == "q":
                menu_choice = Menu.show_pause_menu()

                if menu_choice == "1":
                    continue

                elif menu_choice == "2":
                    return

            else:
                print("Неверная команда. Используйте w, a, s, d или q")


if __name__ == "__main__":
    app = Main()
    app.run()
