from itertools import chain

class Puzzle:
    '''A class representing the board and a node for the heap'''
    def __init__(self, board, parent, level, cost, blank_pos):
        self.board = board
        self.parent = parent
        self.level = level
        self.cost = cost
        self.blank_pos = blank_pos

    def actions(self):
        '''
        Defines legal actions for a board state
        Remove actions that would move blank out of bounds
        Assumes board is square
        '''
        i, j = self.blank_pos
        legal_actions = ['U', 'D', 'L', 'R']

        if i == 0:
            legal_actions.remove('U')
        if i == len(self.board):
            legal_actions.remove('D')
        if j == 0:
            legal_actions.remove('L')
        if j == len(self.board):
            legal_actions.remove('R')

        return legal_actions

    def is_solvable(self):
        '''
        check if puzzle is solvable
        a puzzle is solvable if the number of inversions is even
        returns 0 if solvable, 1 if not
        reference: https://math.stackexchange.com/questions/293527/how-to-check-if-a-8-puzzle-is-solvable
        '''
        inversions = 0
        flattened_board = list(chain.from_iterable(self.board))
        for i, ele in enumerate(flattened_board):
            for later_ele in flattened_board[i+1:]:
                if ele != 0 and later_ele != 0 and ele > later_ele:
                    inversions += 1
        return inversions % 2


