import unittest
import os
import binary_search


class BinarySearchTest(unittest.TestCase):

    def setUp(self):
        self.data_path = os.path.dirname(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        self.data_path = os.path.join(self.data_path, 'algs4-data')
        self.datas = {'file_white': 'tinyW.txt',
                      'file_input': 'tinyT.txt',
                      'ret': [50, 99, 13]}

    def test_search(self):
        fileW = os.path.join(self.data_path, self.datas['file_white'])
        fileT = os.path.join(self.data_path, self.datas['file_input'])
        ret = []
        with open(fileW, 'r') as fw:
            with open(fileT, 'r') as ft:
                a = [int(x) for x in fw.readlines()]
                for x in ft.readlines():
                    k = int(x)
                    if binary_search.binary_search(a, k) < 0:
                        ret.append(k)
        self.assertListEqual(ret, self.datas['ret'])

if __name__ == '__main__':
    unittest.main()
