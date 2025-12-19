class Renderer:
    """Класс для отрисовки лабиринта в консоли."""

    symb = {
        "wall": "██",
        "passage": "  ",
        "player": "☻",
        "exit": "🚩",
    }

    @staticmethod
    def render(maze: list[list[int]], player_position: list, level: int) -> None:
        """Функция, которая отрисовывает лабиринт с игроком и выходом.

        Args:
            maze: Матрица лабиринта.
            player_position: Текущая позиция игрока.
            level: Номер текущего уровня.
        """

        print(f"\n== Уровень {level} ==")
        print()

        for y, row in enumerate(maze):
            line = ""

            for x, cell in enumerate(row):

                if (x, y) == player_position:
                    line += Renderer.symb["player"]

                elif cell == 1:
                    line += Renderer.symb["wall"]

                elif cell == 2:
                    line += Renderer.symb["exit"]

                else:
                    line += Renderer.symb["passage"]

            print(line)

        print('Управление: w - Вверх ↑, s - Вниз ↓, a - Влево ←, d →  - Вправо →, q - Меню/Выход')