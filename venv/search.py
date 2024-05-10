from heapq import heappop, heappush
from itertools import chain

from puzzle import Puzzle

def search(puzzle):
    '''
    Implements general search algorithm
    :param puzzle: initial state
    '''
    nodes_expanded = 0
    max_queue_size = 0
    if puzzle.is_solvable():
        raise Exception("This puzzle is not solvable! Please enter a solvable puzzle.")

    queue = []
    heappush(queue, puzzle)
    #explored_states = {}
    while queue:
        max_queue_size = max(max_queue_size, len(queue))
        current_node = heappop(queue)
        #explored_states[tuple(chain.from_iterable(current_node.board))] = 'explored'
        nodes_expanded += 1
        if current_node.is_goal():
            print(f"Nodes expanded: {nodes_expanded}")
            print(f"Max queue size: {max_queue_size}")
            current_node.print_solution()
            return

        children = current_node.generate_children()
        for child in children:
            # if tuple(chain.from_iterable(child.board)) not in explored_states:
            #     heappush(queue, child)
            heappush(queue, child)