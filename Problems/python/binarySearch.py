#!/usr/bin/env python3

"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        return self.binary_search(nums, target)

    def binary_search(self, input_array, value):
        """Your code goes here."""
        high = len(input_array)-1
        low = 0
        mid = (int)((high + low) / 2)
        while high >= low:
            #print(high, low, mid)
            if (value > input_array[mid]):
                low = mid + 1
            elif (value < input_array[mid]):
                high = mid - 1
            else:
                return mid
            mid = (int)((high + low) / 2)
        return -1

s = Solution()
print(s.search([1,2,3,4,5,6,7,8,9], 5))
print(s.search([1,2,3,4,5,6,7,8,9], 1))
print(s.search([1,2,3,4,5,6,7,8,9], -1))
