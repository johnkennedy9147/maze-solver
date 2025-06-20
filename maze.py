import random
from time import sleep
from shapes import Cell


class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        window=None,
        seed=None,
    ):
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__window = window
        self.__cells = []
        random.seed(seed)
        self.__create_cells()
        self.__break_entrance_and_exit()
        self.__break_walls_r(0, 0)
        self.__reset_cells_visited()

    def __create_cells(self):
        for row in range(self.__num_rows):
            row_cells = []
            for col in range(self.__num_cols):
                cell = Cell(self.__window)
                row_cells.append(cell)
            self.__cells.append(row_cells)
        for row in range(self.__num_rows):
            for col in range(self.__num_cols):
                self.__draw_cell(row, col)

    def __draw_cell(self, i, j):
        x1 = self.__x1 + j * self.__cell_size_x
        y1 = self.__y1 + i * self.__cell_size_y
        x2 = x1 + self.__cell_size_x
        y2 = y1 + self.__cell_size_y
        self.__cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        if self.__window is None:
            return
        self.__window.redraw()
        sleep(0.25)

    def __break_entrance_and_exit(self):
        self.__cells[0][0].has_top_wall = False
        self.__draw_cell(0, 0)
        self.__cells[self.__num_rows - 1][self.__num_cols - 1].has_bottom_wall = False
        self.__draw_cell(self.__num_rows - 1, self.__num_cols - 1)

    def __break_walls_r(self, i, j):
        self.__cells[i][j].visited = True
        while True:
            directions = []
            if i > 0 and not self.__cells[i - 1][j].visited:
                directions.append("up")
            if i < self.__num_rows - 1 and not self.__cells[i + 1][j].visited:
                directions.append("down")
            if j > 0 and not self.__cells[i][j - 1].visited:
                directions.append("left")
            if j < self.__num_cols - 1 and not self.__cells[i][j + 1].visited:
                directions.append("right")

            if not directions:
                return

            direction = random.choice(directions)
            if direction == "up":
                self.__cells[i][j].has_top_wall = False
                self.__cells[i - 1][j].has_bottom_wall = False
                self.__draw_cell(i, j)
                self.__draw_cell(i - 1, j)
                self._animate()
                self.__break_walls_r(i - 1, j)
            elif direction == "down":
                self.__cells[i][j].has_bottom_wall = False
                self.__cells[i + 1][j].has_top_wall = False
                self.__draw_cell(i, j)
                self.__draw_cell(i + 1, j)
                self._animate()
                self.__break_walls_r(i + 1, j)
            elif direction == "left":
                self.__cells[i][j].has_left_wall = False
                self.__cells[i][j - 1].has_right_wall = False
                self.__draw_cell(i, j)
                self.__draw_cell(i, j - 1)
                self._animate()
                self.__break_walls_r(i, j - 1)
            elif direction == "right":
                self.__cells[i][j].has_right_wall = False
                self.__cells[i][j + 1].has_left_wall = False
                self.__draw_cell(i, j)
                self.__draw_cell(i, j + 1)
                self._animate()
                self.__break_walls_r(i, j + 1)

    def __reset_cells_visited(self):
        for row in self.__cells:
            for cell in row:
                cell.visited = False

    def solve(self):
        return self.__solve_r(0, 0)

    def __solve_r(self, i, j):
        self._animate()
        self.__cells[i][j].visited = True

        if i == self.__num_rows - 1 and j == self.__num_cols - 1:
            return True

        # move right
        if (
            j < self.__num_cols - 1
            and not self.__cells[i][j].has_right_wall
            and not self.__cells[i][j + 1].visited
        ):
            self.__cells[i][j].draw_move(self.__cells[i][j + 1])
            if self.__solve_r(i, j + 1):
                return True
            else:
                self.__cells[i][j].draw_move(self.__cells[i][j + 1], undo=True)

        # move down
        if (
            i < self.__num_rows - 1
            and not self.__cells[i][j].has_bottom_wall
            and not self.__cells[i + 1][j].visited
        ):
            self.__cells[i][j].draw_move(self.__cells[i + 1][j])
            if self.__solve_r(i + 1, j):
                return True
            else:
                self.__cells[i][j].draw_move(self.__cells[i + 1][j], undo=True)

        # move left
        if (
            j > 0
            and not self.__cells[i][j].has_left_wall
            and not self.__cells[i][j - 1].visited
        ):
            self.__cells[i][j].draw_move(self.__cells[i][j - 1])
            if self.__solve_r(i, j - 1):
                return True
            else:
                self.__cells[i][j].draw_move(self.__cells[i][j - 1], undo=True)

        # move up
        if (
            i > 0
            and not self.__cells[i][j].has_top_wall
            and not self.__cells[i - 1][j].visited
        ):
            self.__cells[i][j].draw_move(self.__cells[i - 1][j])
            if self.__solve_r(i - 1, j):
                return True
            else:
                self.__cells[i][j].draw_move(self.__cells[i - 1][j], undo=True)

        return False
