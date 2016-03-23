class InsertionSort(object):
    """插入排序"""

    @classmethod
    def less(cls, a, i, j):
        # 比较
        return a[i] < a[j]

    @classmethod
    def exch(cls, a, i, j):
        # 交换
        a[i], a[j] = a[j], a[i]

    @classmethod
    def sort(cls, data):
        print('Using ' + cls.__name__)
        n = len(data)
        for i in range(1, n):
            j = i
            while j > 0 and cls.less(data, j, j-1):
                cls.exch(data, j, j-1)
                j -= 1


def insertion_sort(data):
    n = len(data)
    # 外循环
    for i in range(1, n):
        j = i
        # 对索引i左侧数据排序，保证索引i左侧数据是有序的
        while j > 0 and data[j] < data[j - 1]:
            data[j], data[j - 1] = data[j - 1], data[j]
            j -= 1

if __name__ == '__main__':
    a = ['S', 'O', 'R', 'T', 'E', 'X', 'A', 'M', 'P', 'L', 'E']
    insertion_sort(a)
    print(a)
