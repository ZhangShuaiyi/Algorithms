'''
选择排序
'''


class SelectionSort():
    """docstring for SelectionSort"""

    def __init__(self, arg):
        super(SelectionSort, self).__init__()
        self.arg = arg

    @classmethod
    def exch(cls, a, i, j):
        tmp = a[i]
        a[i] = a[j]
        a[j] = tmp

    @classmethod
    def selection_sort(cls, data):
        print("Using selection_sort!")
        n = len(data)
        for i in range(n):
            min = i
            for j in range(i, n):
                if data[j] < data[min]:
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
