import unittest
from task6 import sorted_nums_repeating_more_than_once


class MyTestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual('0 3 4', sorted_nums_repeating_more_than_once('4 8 0 3 4 2 0 3'))

    def test2(self):
        self.assertEqual('1 2 3', sorted_nums_repeating_more_than_once('1 1 2 2 3 3'))

    def test3(self):
        self.assertEqual('1 2 15 200', sorted_nums_repeating_more_than_once('10 15 15 103 200 200 200 1 1 1 1 1 2 2 2'))


if __name__ == '__main__':
    unittest.main()
