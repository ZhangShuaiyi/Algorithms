## 插入排序
插入排序基本思路，将待排序数据插入已经排序的数据的适当位置

```python
def insertion_sort(data):
    n = len(data)
    # 外循环
    for i in range(1, n):
        j = i
        # 对索引i左侧数据排序，保证索引i左侧数据是有序的
        while j > 0 and data[j] < data[j - 1]:
            data[j], data[j - 1] = data[j - 1], data[j]
            j -= 1
```

![insertion_sort_tiny.gif](https://raw.githubusercontent.com/gonewbee/Algorithms/master/files/insertion_sort_tiny.gif)

### 时间复杂度
对应长度为N数组
+ 倒序的情况，需要(N-1)+(N-2)+...+2+1=N*(N-1)/2次比较和(N-1)+(N-2)+...+2+1=N*(N-1)/2次交换
+ 有序的情况，需要(N-1)次比较和0次交换

时间复杂度为O(n^2)
