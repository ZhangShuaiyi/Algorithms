import os
import sys
from insertion_sort import InsertionSort
_filepath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_filepath = os.path.join(_filepath, 'sort_base')
# 修改sys.path(python环境变量)，添加module搜索目录
sys.path.append(_filepath)
from sort_image import SortImage


class InsertionSortImage(InsertionSort):
    """docstring for InsertionSortImage"""

    @classmethod
    def less(cls, a, i, j):
        cls.sort_image.drawList(text='compare', i=i, j=j, color=(0, 255, 255))
        return super(InsertionSortImage, cls).less(a, i, j)

    @classmethod
    def exch(cls, a, i, j):
        cls.sort_image.drawList(text='swap', i=i, j=j, color=(0, 0, 255))
        super(InsertionSortImage, cls).exch(a, i, j)

    @classmethod
    def sort(cls, a):
        out_path = os.path.dirname(os.path.abspath(__file__))
        out_path = os.path.join(out_path, 'out')
        cls.sort_image = SortImage(a, out_path=out_path)
        super(InsertionSortImage, cls).sort(a)

if __name__ == '__main__':
    import sys
    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()
        a = []
        [a.extend(line.split()) for line in lines]
        InsertionSortImage.sort(a)
        print(a)
