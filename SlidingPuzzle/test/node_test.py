import unittest
from main.node import Node

class NodeTest(unittest.TestCase):

    def test_node_have_a_parent(self):
        numbers_matrix = [[1,2,3],[4,5,6],[7,8,0]]
        node_parent = Node(None, numbers_matrix, 'down')
        node = Node(node_parent, numbers_matrix, 'up')
        self.assertEqual(node_parent, node.get_node_parent())

    def test_node_have_a_numbers_matrix(self):
        numbers_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        node = Node(None, numbers_matrix, 'left')
        self.assertEqual(node.get_numbers_matrix(), numbers_matrix)

    def test_node_have_a_last_movement(self):
        numbers_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        node_parent = Node(None, numbers_matrix, 'right')
        node = Node(node_parent, numbers_matrix, 'up')
        self.assertEqual('up', node.get_last_movement())


if __name__ == '__main__':
        unittest.main()