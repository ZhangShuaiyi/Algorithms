## 希尔排序
希尔排序是插入排序的一种。

+ 确定排序间隔h
+ 按照间隔h对数组排序，保证间隔为h的元素是有序的
+ 缩小h值，再对间隔h数组排序，直到h为1

```python
def shell_sort(a):
    n = len(a)
    h = 1
    while h < n // 3:
        # 计算间隔
        h = 3 * h + 1  # 1, 4, 13

    while h >= 1:
        # 缩小间隔值
        for i in range(h, n):
            # 使用间隔h排序，保证间隔为h的元素是有序的
            j = i
            while j >= h and a[j] < a[j - h]:
                a[j], a[j - h] = a[j - h], a[j]
                j -= h
        h = h // 3
```

![shell_sort_tiny.gif](https://raw.githubusercontent.com/gonewbee/Algorithms/master/files/shell_sort_tiny.gif)
