from puzzle import Puzzle

# hard coded default initial board for testing purposes
# 0 represents the blank tile
default_initial_board = [[0, 4, 6],
                         [3, 8, 7],
                         [2, 5, 1]]

puzzle = Puzzle(default_initial_board)

print(puzzle.is_solvable())