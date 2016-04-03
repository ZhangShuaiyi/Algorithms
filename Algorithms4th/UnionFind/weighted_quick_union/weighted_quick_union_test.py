import unittest
from weighted_quick_union import WeightedQuickUnion
from union_find_test import UnionFindTest

class QuickUnionTest(UnionFindTest, unittest.TestCase):
    """docstring for QuickUnionTest"""
    
    cls = WeightedQuickUnion

if __name__ == '__main__':
    unittest.main()        
