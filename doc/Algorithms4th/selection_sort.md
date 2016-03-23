## 选择排序
+ 找到数组中最小的元素a
+ 将a和数组的第一个元素交换位置（如果第一个元素就是最小的元素那么a就和自己交换）
+ 在剩余的元素中找到最小的元素，将它和数组的第二个元素交换位置
+ 如此往复，直到将整个数组排序

```python
def selection_sort(data):
    n = len(data)
    # 外循环，给第i个位置交换数据
    for i in range(n):
        min = i
        # 内循环，查找最小值
        for j in range(i + 1, n):
            if data[j] < data[min]:
                min = j
        # 交换数据
        data[i], data[min] = data[min], data[i]
```

### 时间复杂度

```python
a = ['S', 'O', 'R', 'T', 'E', 'X', 'A', 'M', 'P', 'L', 'E']
```
比如a长度为11，则比较次数为10+9+8+...+1=11*(11-1)/2=55，交换次数为11。

![selection_sort_tiny.gif](https://raw.githubusercontent.com/gonewbee/Algorithms/master/files/selection_sort_tiny.gif)

对于长度为N数组，需要进行N*(N-1)/2次比较和N次交换，时间复杂度为O(n^2)

### 特点
+ 运行时间和输入无关
+ 数据交换是最少的

[我的示例代码](https://github.com/gonewbee/Algorithms/tree/master/Algorithms4th/Sorting/selection_sort)
