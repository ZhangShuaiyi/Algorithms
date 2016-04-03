import sys
import os
_filePath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_filePath = os.path.join(_filePath, 'union_find_base')
sys.path.append(_filePath)
from union_find_base import UF

class WeightedQuickUnion(UF):
    """加权quick-union算法"""

    def __init__(self, n):
        super(WeightedQuickUnion, self).__init__(n)
        self.sz = [1]*n

    def find(self, p):
        while p != self.id[p]:
            p = self.id[p]
        return p

    def union(self, p, q):
        pRoot = self.find(p)
        qRoot = self.find(q)
        if pRoot == qRoot:
            return
        # 将小树的根节点接到大树的根节点
        if self.sz[pRoot] < self.sz[qRoot]:
            self.id[pRoot] = qRoot
            self.sz[qRoot] += self.sz[pRoot]
        else:
            self.id[qRoot] = pRoot
            self.sz[pRoot] += self.sz[qRoot]
        self.count -= 1