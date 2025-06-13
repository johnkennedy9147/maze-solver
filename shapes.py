class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def draw(self, canvas, fill_color):
        canvas.create_line(
            self.start.x, self.start.y, self.end.x, self.end.y, fill=fill_color, width=2
        )


class Cell:
    def __init__(self, window=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__window = window
        self.__x1 = -1
        self.__y1 = -1
        self.__x2 = -1
        self.__y2 = -1
        self.visited = False

    def draw(self, __x1, __y1, __x2, __y2):
        self.__x1 = __x1
        self.__y1 = __y1
        self.__x2 = __x2
        self.__y2 = __y2

        if self.__window is None:
            return
        if self.has_left_wall:
            self.__window.draw_line(Line(Point(__x1, __y1), Point(__x1, __y2)), "black")
        else:
            self.__window.draw_line(
                Line(Point(__x1, __y1), Point(__x1, __y2)), "#d9d9d9"
            )
        if self.has_right_wall:
            self.__window.draw_line(Line(Point(__x2, __y1), Point(__x2, __y2)), "black")
        else:
            self.__window.draw_line(
                Line(Point(__x2, __y1), Point(__x2, __y2)), "#d9d9d9"
            )
        if self.has_top_wall:
            self.__window.draw_line(Line(Point(__x1, __y1), Point(__x2, __y1)), "black")
        else:
            self.__window.draw_line(
                Line(Point(__x1, __y1), Point(__x2, __y1)), "#d9d9d9"
            )
        if self.has_bottom_wall:
            self.__window.draw_line(Line(Point(__x1, __y2), Point(__x2, __y2)), "black")
        else:
            self.__window.draw_line(
                Line(Point(__x1, __y2), Point(__x2, __y2)), "#d9d9d9"
            )

    def draw_move(self, to_cell, undo=False):
        __colour = "red" if not undo else "gray"
        start_cell_center = Point(
            (self.__x1 + self.__x2) / 2, (self.__y1 + self.__y2) / 2
        )
        end_cell_center = Point(
            (to_cell.__x1 + to_cell.__x2) / 2, (to_cell.__y1 + to_cell.__y2) / 2
        )
        if self.__window is None:
            return
        self.__window.draw_line(Line(start_cell_center, end_cell_center), __colour)
