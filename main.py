from window import Window
from shapes import Cell, Line, Point


def main():
    window = Window(800, 600)

    cell1 = Cell(window)
    cell1.has_right_wall = False
    cell1.draw(50, 50, 150, 150)

    cell2 = Cell(window)
    cell2.has_left_wall = False
    cell2.draw(150, 50, 250, 150)

    cell4 = Cell(window)
    cell4.has_bottom_wall = False
    cell4.draw(300, 50, 400, 150)

    cell5 = Cell(window)
    cell5.has_top_wall = False
    cell5.draw(300, 150, 400, 250)

    cell1.draw_move(cell2)

    cell4.draw_move(cell5, undo=True)
    window.wait_for_close()


main()
