'''
选择排序
'''


def exch(a, i, j):
    tmp = a[i]
    a[i] = a[j]
    a[j] = tmp


def selection_sort(data):
    print("Using selection_sort!")
    n = len(data)
    for i in range(n):
        min = i
        for j in range(i, n):
            if data[j] < data[min]:
                min = j
        exch(data, i, min)


def isSorted(a):
    for i in range(1, len(a)):
        if a[i] < a[i - 1]:
            return False
    return True

if __name__ == '__main__':
    import sys
    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()
        a = []
        [a.extend(line.split()) for line in lines]
        selection_sort(a)
        print(a)
