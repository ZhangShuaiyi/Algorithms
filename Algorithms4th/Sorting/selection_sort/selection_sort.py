'''
选择排序
'''


class SelectionSort():
    """docstring for SelectionSort"""

    @classmethod
    def less(cls, a, i, j):
        # 比较
        return a[i] < a[j]

    @classmethod
    def exch(cls, a, i, j):
        # 交换list
        a[i], a[j] = a[j], a[i]

    @classmethod
    def selection_sort(cls, data):
        print("Using selection_sort!")
        n = len(data)
        # 外循环，给第i个位置交换数据
        for i in range(n):
            min = i
            # 内循环，查找最小值
            for j in range(i+1, n):
                if cls.less(data, j, min):
                    min = j
            cls.exch(data, i, min)

    @classmethod
    def isSorted(cls, a):
        for i in range(1, len(a)):
            if a[i] < a[i - 1]:
                return False
        return True

if __name__ == '__main__':
    import sys
    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()
        a = []
        [a.extend(line.split()) for line in lines]
        SelectionSort.selection_sort(a)
        print(a)
