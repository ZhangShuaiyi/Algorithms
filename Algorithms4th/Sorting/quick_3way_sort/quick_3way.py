class Quick3way():
    """三向切分的快速排序"""

    @classmethod
    def sort(cls, a):
        cls.sort_lh(a, 0, len(a) - 1)

    @classmethod
    def sort_lh(cls, a, lo, hi):
        if hi <= lo:
            return
        lt = lo
        i = lo + 1
        gt = hi
        v = a[lo]
        while i <= gt:
            if a[i] < v:
                a[lt], a[i] = a[i], a[lt]
                lt += 1
                i += 1
            elif a[i] > v:
                a[i], a[gt] = a[gt], a[i]
                gt -= 1
            else:
                i += 1
        # 结果a[lo..lt - 1] < v = a[lt..gt] < a[gt + 1..hi]
        cls.sort_lh(a, lo, lt - 1)
        cls.sort_lh(a, gt + 1, hi)
