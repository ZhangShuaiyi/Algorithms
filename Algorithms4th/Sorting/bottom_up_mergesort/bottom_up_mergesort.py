class MergeBU(object):
    """docstring for MergeBU"""

    @classmethod
    def merge(cls, a, lo, mid, hi):
        # 将a[lo...hi]复制到aux[lo...hi]
        cls.aux[lo:hi + 1] = a[lo:hi + 1]
        i = lo
        j = mid + 1
        k = lo
        # 归并会a[lo...hi]
        while i <= mid and j <= hi:
            if cls.aux[i] < cls.aux[j]:
                a[k] = cls.aux[i]
                k += 1
                i += 1
            else:
                a[k] = cls.aux[j]
                k += 1
                j += 1
        n = mid + 1 - i
        a[k:k + n] = cls.aux[i:mid + 1]
        k += n
        n = hi + 1 - j
        a[k:k + n] = cls.aux[j:hi + 1]

    @classmethod
    def sort(cls, a):
        # lgN次两两归并
        n = len(a)
        cls.aux = [0] * n
        # sz子数组大小
        sz = 1
        while sz < n:
            # lo子数组索引
            lo = 0
            while lo < n - sz:
                cls.merge(a, lo, lo + sz - 1, min(lo + sz + sz - 1, n - 1))
                lo += (sz + sz)
            sz += sz
