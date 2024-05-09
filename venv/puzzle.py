from itertools import chain

class Puzzle:
    def __init__(self, board):
        self.board = board

    '''
    check if puzzle is initially solvable
    a puzzle is solvable if the number of inversions is even
    returns 0 if solvable, 1 if not
    reference: https://math.stackexchange.com/questions/293527/how-to-check-if-a-8-puzzle-is-solvable
    '''
    def is_solvable(self):
        inversions = 0
        flattened_board = list(chain.from_iterable(self.board))
        for i, ele in enumerate(flattened_board):
            for later_ele in flattened_board[i+1:]:
                if ele != 0 and later_ele != 0 and ele > later_ele:
                    inversions += 1

        return inversions % 2


