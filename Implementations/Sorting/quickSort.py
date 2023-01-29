#!/usr/bin/env python3
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    result = quick_sort(left) + middle + quick_sort(right)
    print(result)
    return result

print(quick_sort([3,2,4,1,8,6,2]))
