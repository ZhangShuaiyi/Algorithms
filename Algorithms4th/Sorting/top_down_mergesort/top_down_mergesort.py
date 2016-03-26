class TopDownMergeSort():
    """自顶向下的归并排序"""

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
        a[k:k+n] = cls.aux[i:mid+1]
        k += n
        n = hi + 1 - j
        a[k:k+n] = cls.aux[j:hi+1]

    @classmethod
    def merge_sort(cls, a, lo, hi):
        if hi <= lo:
            return
        mid = lo + (hi - lo) // 2
        # 对左侧进行排序
        cls.merge_sort(a, lo, mid)
        # 对右侧进行排序
        cls.merge_sort(a, mid + 1, hi)
        # 归并结果
        cls.merge(a, lo, mid, hi)

    @classmethod
    def sort(cls, a):
        n = len(a)
        cls.aux = [0] * n
        cls.merge_sort(a, 0, n-1)

if __name__ == '__main__':
    a = ['S', 'O', 'R', 'T', 'E', 'X', 'A', 'M', 'P', 'L', 'E']
    TopDownMergeSort.sort(a)
    print(a)
