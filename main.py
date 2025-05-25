from window import Window
from shapes import Line, Point


def main():
    window = Window(800, 600)

    start_point = Point(100, 100)
    end_point1 = Point(200, 100)
    end_point2 = Point(100, 200)
    
    line1 = Line(start_point, end_point1)
    line2 = Line(start_point, end_point2)
    
    window.draw_line(line1, "red")
    window.draw_line(line2, "blue")

    window.wait_for_close()


main()
