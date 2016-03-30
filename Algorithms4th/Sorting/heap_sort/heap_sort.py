class HeapSort():
    """堆排序"""

    @classmethod
    def swim(cls, a, k, n):
        '''
        由下至上的堆有序化（上浮）的实现
        '''
        # 父节点为(k-1)//2
        j = (k-1) // 2
        while k > 0 and a[j] < a[k]:
            a[j], a[k] = a[k], a[j]
            k = j
            j = (k-1) // 2

    @classmethod
    def sink(cls, a, k, n):
        '''
        由上至下的堆有序化（下沉）的实现
        '''
        # 子节点为2*k+1 和2*k-1
        j = 2*k + 1
        while j <= n:
            if j < n and a[j] < a[j+1]:
                j += 1
            if a[k] >= a[j]:
                break
            a[k], a[j] = a[j], a[k]
            k = j
            j = 2*k + 1

    @classmethod
    def sort(cls, a):
        n = len(a)-1
        # 堆有序化，堆有序后a[0]为最大值
        for k in range((n-1)//2, -1, -1):
            cls.sink(a, k, n)
        while n > 0:
            # a[0]最大，将a[0]交换到最后
            a[0], a[n] = a[n], a[0]
            n -= 1
            # 减小堆大小，将a[0]下浮到对应位置
            cls.sink(a, 0, n)
