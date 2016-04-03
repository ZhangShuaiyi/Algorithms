import unittest
from quick_union import QuickUnion
from union_find_test import UnionFindTest

class QuickUnionTest(UnionFindTest, unittest.TestCase):
    """docstring for QuickUnionTest"""
    
    cls = QuickUnion

if __name__ == '__main__':
    unittest.main()        
