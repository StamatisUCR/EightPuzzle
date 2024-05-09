from itertools import chain
from math import floor

# calculates number of tiles that are not in their final place
def misplaced_tile(board):
    misplaced_tiles = 0
    flattened_board = list(chain.from_iterable(board))
    for i, ele in enumerate(flattened_board, start=1):
        if ele != 0 and ele != i:
            misplaced_tiles += 1
        elif ele == 0 and i != len(flattened_board):
            misplaced_tiles += 1
    return misplaced_tiles

def manhattan_distance(board):
    board_width = len(board[0]) # assume board is square (3x3, 4x4, etc)
    distance = 0
    for i, row in enumerate(board):
        for j, ele in enumerate(row):
            if ele == 0:
                ele = board_width * board_width # blank belongs in last space, this is needed for the following trick

            # can easily determine goal location using division and modulo
            ele_goal_row = floor((ele-1)/board_width)
            ele_goal_column = (ele-1) % board_width
            distance += abs(i - ele_goal_row) + abs(j - ele_goal_column)
    return distance

