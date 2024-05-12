
# MAZE TESTS
# Unit tests are generally a great idea. Let's add a couple. 
# In order to be able to test some of our Maze class's methods, 
# we need to be able to run the logic without actually drawing anything graphically. 
# We want to test the logic, not the visuals at this point.
    # make the Window parameter to the Cell and Maze class optional, and have it default to None.
    
# WRITING TESTS IN PYTHON
    # First, create a tests.py file. We'll be using the unittest package for our testing, 
    # so add the following to the top of tests.py:
    
import unittest

# next, import Maze code:
from maze import Maze

# Then create a simple test:
class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )
#### 8.MAZE test
# Add some code to make the test run:
#    def test_maze_create_cells_large(self):
 #       num_cols = 16
  #      num_rows = 12
   #     m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
    #    self.assertEqual(
     #       len(m1._cells),
      #      num_cols,
       # )

#### 9.BREAKING DOWN WALLS IN THE MAZE
    def test_maze_break_entrance_and_exit(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            m1._cells[0][0].has_top_wall,
            False,
        )
        self.assertEqual(
            m1._cells[num_cols - 1][num_rows - 1].has_bottom_wall,
            False,
        )
    
    def test_maze_reset_cells_visited(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        for col in m1._cells:
            for cell in col:
                self.assertEqual(
                    cell.visited,
                    False,
                )
        
if __name__ == "__main__":
    unittest.main()

# Finally, run the tests:
    # python tests.py

'''
If everything worked with that one test, great! 
Add a couple more tests to make sure your maze constructor works under different conditions. 
You can do so by adding new methods to the Tests class. 
Your new tests should create a new maze but use different numbers of rows and columns. 
Use the assertEqual method again to check that everything worked.
'''

    
    