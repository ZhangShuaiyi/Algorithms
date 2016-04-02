import sys
import os
_filepath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_filepath = os.path.join(_filepath, 'union_find_base')
# 修改sys.path(python环境变量)，添加module搜索目录
sys.path.append(_filepath)
from union_find_base import UF

class QuickFind(UF):
    """docstring for QuickFind"""

    def find(self, p):
        return self.id[p]

    def union(self, p, q):
        pID = self.find(p)
        qID = self.find(q)

        if pID == qID:
            return
        for i, v in enumerate(self.id):
            if v == pID:
                self.id[i] = qID
        self.count -= 1
