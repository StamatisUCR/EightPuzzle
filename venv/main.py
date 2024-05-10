from puzzle import Puzzle
from search import search
from heuristics import misplaced_tile, manhattan_distance

def find_blank(board):
    blank_pos = ()
    for i, row in enumerate(board):
        for j, ele in enumerate(row):
            if ele == 0:
                blank_pos = (i, j)
    return blank_pos

# hard coded default initial board for testing purposes
# 0 represents the blank tile
default_initial_board = [[0, 4, 6],
                         [3, 8, 7],
                         [2, 5, 1]]


# Test cases from project description
# depth = 0
trivial = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 0]]

# depth = 2
very_easy = [[1, 2, 3],
             [4, 5, 6],
             [0, 7, 8]]

# depth = 4
easy = [[1, 2, 3],
        [5, 0, 6],
        [4, 7, 8]]

# depth = 8
medium = [[1, 3, 6],
          [5, 0, 2],
          [4, 7, 8]]

# depth = 12
slightly_hard = [[1, 3, 6],
                 [5, 0, 7],
                 [4, 8, 2]]

# depth = 16
hard = [[1, 6, 7],
        [5, 0, 3],
        [4, 8, 2]]

# depth = 20
very_hard = [[7, 1, 2],
             [4, 8, 5],
             [6, 3, 0]]

# depth = 24
impossible = [[0, 7, 2],
              [4, 6, 1],
              [3, 5, 8]]

def main():
    choice = input("Welcome to my Eight Puzzle solver. Type '1' to use a default puzzle. Type '2' to input your own puzzle. \n")
    if choice == '1':
        board = default_initial_board
    elif choice == '2':
        board = []
        print("Ok! Use 0 to represent the blank space. Please input a valid puzzle. Use only numbers 0-9, using each number once.")
        first_row = input("Please input the first row separated by spaces. Please input only 3 numbers. \n")
        second_row = input("Please input the second row separated by spaces. Please input only 3 numbers. \n")
        third_row = input("Please input the third row separated by spaces. Please input only 3 numbers. \n")

        first_row = first_row.split()
        second_row = second_row.split()
        third_row = third_row.split()
        board.append([int(num) for num in first_row])
        board.append([int(num) for num in second_row])
        board.append([int(num) for num in third_row])
    else:
        raise Exception("Please enter a valid choice next time.")

    choice = input("Great! Now please choose your search algorithm. Type '1' for Uniform Cost Search. Type '2' for A* search. \n")
    search_alg = None
    heuristic = None
    heuristic_distance = None
    if choice == '1':
        heuristic_distance = 0
    elif choice == '2':
        choice = input("Great! Please choose your heuristic. Type '1' for misplaced tile. Type '2' for manhattan distance. \n")
        if choice == '1':
            heuristic = 'misplaced'
            heuristic_distance = misplaced_tile(board)
        elif choice == '2':
            heuristic = 'manhattan'
            heuristic_distance = manhattan_distance(board)
        else:
            raise Exception("Please enter a valid choice next time.")
    else:
        raise Exception("Please enter a valid choice next time.")

    blank_pos = find_blank(board)
    puzzle = Puzzle(board, None, 0, blank_pos, heuristic, heuristic_distance)

    print("Searching...")
    search(puzzle)

if __name__ == "__main__":
    main()
