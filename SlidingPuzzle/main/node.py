class Node:

    node_parent = None
    number_matrix = None
    last_movement = None

    def __init__(self, node_parent, numbers_matrix, last_movement):
        self.node_parent = node_parent
        self.number_matrix = numbers_matrix
        self.last_movement = last_movement

    def get_node_parent(self):
        return self.node_parent

    def get_numbers_matrix(self):
        return self.number_matrix

    def get_last_movement(self):
        return self.last_movement


