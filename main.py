from window import Window
from shapes import Cell, Line, Point


def main():
    window = Window(800, 600)

    start_point = Point(100, 100)
    end_point1 = Point(200, 100)
    end_point2 = Point(100, 200)

    line1 = Line(start_point, end_point1)
    line2 = Line(start_point, end_point2)

    window.draw_line(line1, "red")
    window.draw_line(line2, "blue")

    cell1 = Cell(window)
    cell1.draw(50, 50, 150, 150)

    cell2 = Cell(window)
    cell2.has_left_wall = False
    cell2.draw(200, 50, 300, 150)

    cell3 = Cell(window)
    cell3.has_right_wall = False
    cell3.draw(350, 50, 450, 150)

    cell4 = Cell(window)
    cell4.has_top_wall = False
    cell4.draw(500, 50, 600, 150)

    cell5 = Cell(window)
    cell5.has_bottom_wall = False
    cell5.draw(650, 50, 750, 150)

    window.wait_for_close()


main()
