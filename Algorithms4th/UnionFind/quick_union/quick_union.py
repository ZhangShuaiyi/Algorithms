import sys
import os
_filePath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_filePath = os.path.join(_filePath, 'union_find_base')
sys.path.append(_filePath)
from union_find_base import UF

class QuickUnion(UF):
    """docstring for QuickUnion"""

    def find(self, p):
        while p != self.id[p]:
            p = self.id[p]
        return p

    def union(self, p, q):
        pRoot = self.find(p)
        qRoot = self.find(q)
        if pRoot == qRoot:
            return
        self.id[pRoot] = qRoot
        self.count -= 1
        
