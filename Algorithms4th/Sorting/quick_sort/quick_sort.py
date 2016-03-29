class QuickSort(object):
    """快速排序"""

    @classmethod
    def sort(cls, a):
        cls.sort_lh(a, 0, len(a) - 1)

    @classmethod
    def partition(cls, a, lo, hi):
        # 左右扫描索引
        i = lo
        j = hi + 1
        # 切分元素
        v = a[lo]
        while True:
            # 扫描左右，检查扫描是否结束并交换元素
            i += 1
            while a[i] < v:
                if i == hi:
                    break
                i += 1
            j -= 1
            while v < a[j]:
                if j == lo:
                    break
                j -= 1
            if i >= j:
                break
            a[i], a[j] = a[j], a[i]
        a[lo], a[j] = a[j], a[lo]
        # 结果a[lo..j-1] <= a[j] <= a[j+1..hi]
        return j

    @classmethod
    def sort_lh(cls, a, lo, hi):
        if hi <= lo:
            return
        j = cls.partition(a, lo, hi)
        cls.sort_lh(a, lo, j - 1)
        cls.sort_lh(a, j + 1, hi)
