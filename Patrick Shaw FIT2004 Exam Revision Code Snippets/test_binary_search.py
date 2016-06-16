import unittest
from binary_search import *

class BinarySearchTest(unittest.TestCase):
    test_list_4_len = 400
    test_list_1 = []
    test_list_2 = [1]
    test_list_3 = [1,2]
    test_list_4 = [x for x in range(test_list_4_len)]

    def test_binary_search_iterative(self):
        self.assertIsNone(binary_search_iterative(BinarySearchTest.test_list_1, 0))

        self.assertIsNone(binary_search_iterative(BinarySearchTest.test_list_2, -1))
        self.assertEqual(binary_search_iterative(BinarySearchTest.test_list_2, 1), 0)

        self.assertEqual(binary_search_iterative(BinarySearchTest.test_list_3, 1), 0)
        self.assertEqual(binary_search_iterative(BinarySearchTest.test_list_3, 2), 1)

        for i in range(BinarySearchTest.test_list_4_len):
            self.assertEqual(binary_search_iterative(BinarySearchTest.test_list_4, i), i)

    def test_binary_search_recursive(self):
        self.assertIsNone(binary_search(BinarySearchTest.test_list_1, 0))

        self.assertIsNone(binary_search(BinarySearchTest.test_list_2, -1))
        self.assertEqual(binary_search(BinarySearchTest.test_list_2, 1), 0)

        self.assertEqual(binary_search(BinarySearchTest.test_list_3, 1), 0)
        self.assertEqual(binary_search(BinarySearchTest.test_list_3, 2), 1)

        for i in range(BinarySearchTest.test_list_4_len):
            self.assertEqual(binary_search(BinarySearchTest.test_list_4, i), i)