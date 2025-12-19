import random


class MazeGenerator:
    """Класс для генерации лабиринта алгоритмом рекурсивный backtracking"""

    def __init__(self, width: int, height: int) -> None:
        """Инициализирует размеры лабиринта.

           Args:
                width: Ширина лабиринта.
                height: Высота лабиринта.
           """

        if width % 2 == 0:
            width += 1

        if height % 2 == 0:
            height += 1

        self.width = width
        self.height = height

    def generate_maze(self) -> list[list[int]]:
        """Функция, которая генерирует карту лабиринта.

        Returns:
                map: Матрица (карта) лабиринта, где 0 — проход, 1 — стена, 2 — выход.
        """

        map = [[1 for _ in range(self.width)] for _ in range(self.height)]
        start_x, start_y = 1, 1
        start_position = (start_x, start_y)
        map[start_y][start_x] = 0
        stack = [start_position]
        visited = set(stack)

        while stack:
            cx, cy = stack[-1]
            map[cx][cy] = 0
            directions = [(-2, 0), (0, 2), (2, 0), (0, -2)]
            random.shuffle(directions)
            found = False

            for dx, dy in directions:
                nx, ny = cx + dx, cy + dy
                between_x, between_y = cx + dx // 2, cy + dy // 2

                if 0 <= nx < self.height and 0 <= ny < self.width and (nx, ny) not in visited:
                    if 0 <= between_x < self.height and 0 <= between_y < self.width:
                        map[between_x][between_y] = 0
                    map[nx][ny] = 0
                    visited.add((nx, ny))
                    stack.append((nx, ny))
                    found = True
                    break

            if not found:
                stack.pop()

        map[self.height - 2][self.width - 2] = 2

        return map
