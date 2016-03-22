import unittest
import os
from selection_sort import SelectionSort


class TestSelectionSort(unittest.TestCase):

    def setUp(self):
        self.data_path = os.path.dirname(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        self.datas = [
            {"algs4-data/tiny.txt":
             ['A', 'E', 'E', 'L', 'M', 'O', 'P', 'R', 'S', 'T', 'X']},
            {"algs4-data/words3.txt":
             ['all', 'bad', 'bed', 'bug', 'dad', 'dim', 'dug', 'egg',
              'fee', 'few', 'for', 'gig', 'hut', 'ilk', 'jam', 'jay',
              'jot', 'joy', 'men', 'nob', 'now', 'owl', 'rap', 'sky',
              'sob', 'tag', 'tap', 'tar', 'tip', 'wad', 'was', 'wee',
              'yes', 'yet', 'zoo']}
        ]

    def test_sort(self):
        for item in self.datas:
            for filename, ret in item.items():
                print('Reading ' + filename)
                a = []
                with open(os.path.join(self.data_path, filename), 'r') as f:
                    lines = f.readlines()
                    [a.extend(line.split()) for line in lines]
                SelectionSort.selection_sort(a)
                self.assertListEqual(a, ret)


if __name__ == '__main__':
    unittest.main()
