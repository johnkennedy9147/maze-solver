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
        win,
    ):
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win
        self.__cells = []
        self.__create_cells()

    def __create_cells(self):
        for row in range(self.__num_rows):
            row_cells = []
            for col in range(self.__num_cols):
                cell = Cell(self.__win)
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
        self.__win.redraw()
        sleep(0.05)
