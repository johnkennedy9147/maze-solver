from tkinter import Tk, BOTH, Canvas
from shapes import Line


class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__root.geometry(f"{width}x{height}")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__canvas = Canvas(self.__root)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running = False

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.runnning = True
        while self.runnning:
            self.redraw()

    def close(self):
        self.runnning = False

    def draw_line(self, line, fill_color):
        line.draw(self.__canvas, fill_color)
