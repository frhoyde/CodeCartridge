#!/usr/bin/env python3

def mergeSort(arr):
    if len(arr) <= 1:
        return arr

    # divide array into two halves
    middle = len(arr)//2
    left_half = arr[:middle]
    right_half = arr[middle:]

    # recursively sort each half
    left_half = mergeSort(left_half)
    right_half = mergeSort(right_half)

    # merge the two sorted halves back together
    return merge(left_half, right_half)

def merge(left, right):
    result = []
    left_index = 0
    right_index = 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1
    result += left[left_index:]
    result += right[right_index:]
    return result



print(mergeSort([1,2,4,8,7,3,5,6]))
