from render import Renderer


class MazeGame:
    """Класс для управления одним уровнем игры."""

    def __init__(self, maze: list[list[int]], start_position: list, exit_position: tuple) -> None:
        """"Инициализирует игровой уровень.

        Args:
            maze: Матрица лабиринта.
            start_position: Стартовая позиция игрока.
            exit_position: Позиция выхода из лабиринта.
        """

        self.maze = maze
        self.player_position = [start_position[1], start_position[0]]
        self.exit_position = (exit_position[1], exit_position[0])
        self.start_position = [start_position[1], start_position[0]]

    def move(self, direction_of_movement) -> tuple:
        """Функция, которая перемещает игрока в указанном направлении, если возможно.

        Аargs:
            direction_of_movement: Направление движения (вверх, вниз, вправо, влево).

        Returns:
            tuple(int, int): Новая позиция игрока.
        """

        dx, dy = 0, 0

        if direction_of_movement == "w":
            dy = -1

        elif direction_of_movement == "s":
            dy = 1

        elif direction_of_movement == "a":
            dx = -1

        elif direction_of_movement == "d":
            dx = 1

        new_x = self.player_position[0] + dx
        new_y = self.player_position[1] + dy

        if ((0 <= new_x < len(self.maze[0])) and (0 <= new_y < len(self.maze)) and (self.maze[new_y][new_x] != 1)):
            self.player_position = [new_x, new_y]

        return (self.player_position[0], self.player_position[1])

    def is_winner(self) -> bool:
        """Функция, которая проверяет, дошел ли игрок до выхода.

        Returns:
            bool: True, если игрок на выходе, иначе False.
        """

        return (self.player_position[0], self.player_position[1]) == self.exit_position

    def render(self, level: int) -> None:
        """Функция, которая отображает текущее состояние уровня.

        Args:
            level: Номер текущего уровня.
        """

        Renderer.render(self.maze, tuple(self.player_position), level)
