# unitesting cases
import unittest
from Assignment3 import Particular, graph

class TestPath(unittest.TestCase):
    # test1- is path result is list?
    def test_particular_path(self):
        result = Particular(1, graph).particular_paths('A', 'D', ['A', 'E', 'B', 'C', 'D'])
        self.assertEqual(type(result), list)

    def test_minimum_path(self):
        result = Particular(2, graph).min_path('A', 'C')
        # checking that minimum path is a list
        self.assertFalse(type(result) == tuple)

    def test_particular_path_1(self):
        result=Particular(3, graph).particular_paths('A', 'D', ['A', 'E', 'B', 'C', 'D'])
        self.assertNotIsInstance(result, int)

if __name__ == '__main__':
    unittest.main()