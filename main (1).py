from sudoku import Sudoku

# Initializes a Sudoku puzzle with 3 x 3 sub-grid and
# generates a puzzle with half of the cells empty
puzzle = Sudoku(3).difficulty(0.5)
puzzle.show()
print("..........and the solutions..........")
print(puzzle.solve())
