from itertools import chain
from copy import deepcopy

from heuristics import misplaced_tile, manhattan_distance

class Puzzle:
    '''A class representing the board and a node for the heap'''
    def __init__(self, board, parent, level, blank_pos, heuristic, heuristic_cost):
        self.board = board
        self.parent = parent
        self.level = level
        self.blank_pos = blank_pos
        self.heuristic = heuristic
        self.heuristic_cost = None
        if heuristic is not None:
            self.heuristic_cost = heuristic_cost

    def __lt__(self, other):
        '''
        Defines comparison of different puzzles
        :param other: another puzzle instance
        '''
        self_cost = self.level
        other_cost = other.level
        if heuristics is not None:
            self_cost += self.heuristic_cost
            other_cost += other.heuristic_cost
        return self_cost < other_cost

    def actions(self):
        '''
        Defines legal actions for a board state
        Remove actions that would move blank out of bounds
        Assumes board is square
        :return: list of char strings of legal actions
        '''
        i, j = self.blank_pos
        legal_actions = ['U', 'D', 'L', 'R']

        if i == 0:
            legal_actions.remove('U')
        if i == len(self.board) - 1:
            legal_actions.remove('D')
        if j == 0:
            legal_actions.remove('L')
        if j == len(self.board) - 1:
            legal_actions.remove('R')

        return legal_actions

    def calculate_heuristic_cost(self):
        '''
        :return: h(n) for the puzzle
        '''
        cost = 0
        if self.heuristic is None:
            cost = 0
        elif self.heuristic == 'misplaced':
            cost = misplaced_tile(self.board)
        elif self.heuristic == 'manhattan':
            cost = manhattan_distance(self.board)
        else:
            raise Exception("Please enter a valid heuristic. Can be None, misplaced, or manhattan")

        return cost

    def generate_children(self):
        '''
        Generates possible puzzles from current puzzle
        :return: list of child puzzles
        '''
        children = []
        for action in self.actions():
            child = deepcopy(self)
            child.parent = self
            child.level = self.level + 1
            i, j = self.blank_pos
            if action == 'U':
                child.blank_pos = (i-1, j)
                child.board[i][j], child.board[i-1][j] = child.board[i-1][j], child.board[i][j]
            elif action == 'D':
                child.blank_pos = (i + 1, j)
                child.board[i][j], child.board[i+1][j] = child.board[i+1][j], child.board[i][j]
            elif action == 'L':
                child.blank_pos = (i, j - 1)
                child.board[i][j], child.board[i][j-1] = child.board[i][j-1], child.board[i][j]
            elif action == 'R':
                child.blank_pos = (i, j + 1)
                child.board[i][j], child.board[i][j+1] = child.board[i][j+1], child.board[i][j]

            child.heuristic_cost = child.calculate_heuristic_cost()
            children.append(child)
        return children

    def is_solvable(self):
        '''
        check if puzzle is solvable
        a puzzle is solvable if the number of inversions is even
        reference: https://math.stackexchange.com/questions/293527/how-to-check-if-a-8-puzzle-is-solvable
        :return: 0 if solvable, 1 if not
        '''
        inversions = 0
        flattened_board = list(chain.from_iterable(self.board))
        for i, ele in enumerate(flattened_board):
            for later_ele in flattened_board[i+1:]:
                if ele != 0 and later_ele != 0 and ele > later_ele:
                    inversions += 1
        return inversions % 2

    def is_goal(self):
        '''
        Tests if board is in the goal state
        :return: True if the board is the goal, False o/w
        '''
        misplaced_tiles = misplaced_tile(self.board)
        if misplaced_tiles == 0:
            return True
        return False

    def display(self):
        print(f"g(n) = {self.level}, h(n) = {self.heuristic_cost}")
        for row in self.board:
            print(row)

    def print_solution(self):
        '''
        Follow chain of parents to print final solution path
        '''
        solution = [self]
        while self.parent is not None:
            solution.append(self.parent)
            self = self.parent

        for puzzle in reversed(solution):
            puzzle.display()
