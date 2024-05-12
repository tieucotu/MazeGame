#7. Maze class
from graphics import Window
#from cell import Cell
from maze import Maze
import sys

def main():
    num_rows = 12
    num_cols = 16
    margin = 50
    screen_x = 800
    screen_y = 600
    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows

    sys.setrecursionlimit(10000)
    win = Window(screen_x, screen_y)

    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win, 10)
    print("maze created")
    is_solveable = maze.solve()
    if not is_solveable:
        print("maze can not be solved!")
    else:
        print("maze solved!")
    win.wait_for_close()


main()



'''
#6. CELL DRAW_MOVE() METHOD
# ------------------------------------
from graphics import Window
from cell import Cell

def main():
    win = Window(800, 600)
    
    c1 = Cell(win)
    c1.has_right_wall = False
    c1.draw(50, 50, 100, 100)
    
    c2 = Cell(win)
    c2.has_left_wall = False
    c2.has_bottom_wall = False
    c2.draw(100, 50, 150, 100)
    
    c1.draw_move(c2)
    
    c3 = Cell(win)
    c3.has_top_wall = False
    c3.has_right_wall = False
    c3.draw(100, 100, 150, 150)
    
    c2.draw_move(c3)
    
    c4 = Cell(win)
    c4.has_left_wall = False
    c4.draw(150, 100, 200, 150)
    
    c3.draw_move(c4, True)
    
# Đây là code của graphics trước khi tạo class Cell.
    # Draw a few lines using your new methods. 
    # You'll need to draw after you've created an instance of a Window, but before you call wait_for_close().
    # l = Line(Point(50, 50), Point(400, 400))
    # win.draw_line(1, "black")
    
    win.wait_for_close()
    
main()

'''