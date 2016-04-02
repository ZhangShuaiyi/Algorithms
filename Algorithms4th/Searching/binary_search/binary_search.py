def binary_search(a, k):
    a.sort()
    lo = 0
    hi = len(a) - 1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if k < a[mid]:
            hi = mid - 1
        elif k > a[mid]:
            lo = mid + 1
        else:
            return mid
    return -1
