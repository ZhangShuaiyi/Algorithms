import unittest
from quick_find import QuickFind
from union_find_test import UnionFindTest

class QuickFindTest(UnionFindTest, unittest.TestCase):
    """docstring for QuickFindTest"""

    cls = QuickFind

if __name__ == '__main__':
    unittest.main()
