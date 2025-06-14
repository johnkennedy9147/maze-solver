from maze import Maze
from window import Window


def main():
    num_rows = 10
    num_cols = 10
    margin = 50
    screen_x = 800
    screen_y = 600
    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows
    win = Window(screen_x, screen_y)

    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win, seed=1)

    print("Maze created - attempting to solve.")
    solveable = maze.solve()
    if solveable:
        print("Maze is solvable.")
    else:
        print("Maze is not solvable.")

    win.wait_for_close()


main()
