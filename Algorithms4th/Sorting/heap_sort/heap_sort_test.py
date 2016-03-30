import unittest
import os
import sys
from heap_sort import HeapSort
_filepath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_filepath = os.path.join(_filepath, 'sort_base')
# 修改sys.path(python环境变量)，添加module搜索目录
sys.path.append(_filepath)
from sort_test import TestSort


class TestInsertionSort(TestSort, unittest.TestCase):
    """
    使用多重继承(multiple inheritance)的方式，使用Test基类
    http://stackoverflow.com/questions/1323455/python-unit-test-with-base-and-sub-class
    要想定义的setUp也生效，将unittest.TestCase放在后面
    """

    cls = HeapSort

if __name__ == '__main__':
    unittest.main()
