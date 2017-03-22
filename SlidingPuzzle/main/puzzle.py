import sys
import bisect
from input_converter import InputConverter
from node import Node
from movement_evaluator import MovementEvaluator
from solution_verifier import SolutionVerifier
from matrix_updater import MatrixUpdater
from binary_search import BinarySearch
from matrix_printer import MatrixPrinter

user_input = sys.argv[1]
input_converter = InputConverter()
movement_evaluator = MovementEvaluator()
solution_verifier = SolutionVerifier()
matrix_updater = MatrixUpdater()
user_input_list = input_converter.convert_input(user_input)
matrix = input_converter.create_matrix(user_input_list)
binary_searcher = BinarySearch()
matrix_printer = MatrixPrinter()

if solution_verifier.has_solution(matrix):

    initial_node = Node(None, matrix, None)
    explored_nodes_matrix = []
    frontier_sorted_nodes = [] #this list will save the nodes converted to numbers
    frontier_nodes = []

    explored_nodes_matrix.append(binary_searcher.convert_matrix_to_number(initial_node.get_numbers_matrix()))
    frontier_nodes.insert(0, initial_node)
    solution_node = None

    while len(frontier_nodes)>0 and solution_node == None:
        current_node = frontier_nodes.pop()
        bisect.insort(explored_nodes_matrix, binary_searcher.convert_matrix_to_number(current_node.get_numbers_matrix()))
        if not solution_verifier.is_solution(current_node.get_numbers_matrix()):
            movements_list = movement_evaluator.get_possible_movements(current_node.get_numbers_matrix())
            for movement in movements_list:
                updated_matrix = matrix_updater.update_matrix(current_node.get_numbers_matrix(), movement)
                explored_node = False #for each node is initialize in false
                frontier_node = False #for each node is initialize in false
                if binary_searcher.do_search(explored_nodes_matrix, updated_matrix) or binary_searcher.do_search(frontier_sorted_nodes, updated_matrix):
                    explored_node = True
                if not explored_node:
                    new_node = Node(current_node, updated_matrix, movement)
                    frontier_nodes.insert(0, new_node)
                    bisect.insort(frontier_sorted_nodes,
                                  binary_searcher.convert_matrix_to_number(new_node.get_numbers_matrix()))
        else:
            solution_node = current_node

    if solution_node != None:
        parents_matrix_list = []
        parents_movement_list = []
        parents_matrix_list.append(solution_node.get_numbers_matrix())
        parents_movement_list.append(solution_node.get_last_movement())

        solution_node_parent = solution_node.get_node_parent()
        while solution_node_parent != None:
            parents_matrix_list.append(solution_node_parent.get_numbers_matrix())
            parents_movement_list.append(solution_node_parent.get_last_movement())
            solution_node_parent = solution_node_parent.get_node_parent()

        parents_movement_list.pop()
        parents_matrix_list.reverse()
        parents_movement_list.reverse()

        matrix_printer.print_matrix(parents_matrix_list[0])
        for i in range(1, len(parents_matrix_list)):
            print parents_movement_list[i-1]
            matrix_printer.print_matrix(parents_matrix_list[i])

    else:
        print 'This puzzle has no solution!'

    total_moves_str = 'TOTAL MOVES: '
    total_moves_str += str(len(parents_movement_list))
    total_evaluated_nodes = 'EVALUATED NODES: '
    total_evaluated_nodes += str(len(explored_nodes_matrix))
    print '\n'
    print total_moves_str
    print total_evaluated_nodes

else:
    print 'This puzzle has no solution!'


