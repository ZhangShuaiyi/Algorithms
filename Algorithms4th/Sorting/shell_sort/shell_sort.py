class ShellSort(object):
    """希尔排序"""

    @classmethod
    def less(cls, a, i, j):
        # 比较
        return a[i] < a[j]

    @classmethod
    def exch(cls, a, i, j):
        # 交换
        a[i], a[j] = a[j], a[i]

    @classmethod
    def sort(cls, a):
        n = len(a)
        h = 1
        while h < n // 3:
            h = 3 * h + 1  # 1, 4, 13

        while h >= 1:
            for i in range(h, n):
                j = i
                while j >= h and cls.less(a, j, j - h):
                    cls.exch(a, j, j - h)
                    j -= h
            h = h // 3


def shell_sort(a):
    n = len(a)
    h = 1
    while h < n // 3:
        # 计算间隔
        h = 3 * h + 1  # 1, 4, 13

    while h >= 1:
        # 缩小间隔值
        for i in range(h, n):
            j = i
            # 使用间隔h排序，保证间隔为h的元素是有序的
            while j >= h and a[j] < a[j - h]:
                a[j], a[j - h] = a[j - h], a[j]
                j -= h
        h = h // 3

if __name__ == '__main__':
    a = ['S', 'O', 'R', 'T', 'E', 'X', 'A', 'M', 'P', 'L', 'E']
    shell_sort(a)
    print(a)
