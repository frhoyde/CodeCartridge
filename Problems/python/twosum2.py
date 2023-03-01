#!/usr/bin/env python3

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = len(numbers) - 1
        while i >= 0:
            num = target - numbers[i]
            j = self.binarySearch(numbers, i, num)
            if j != -1:
                return [j+1, i+1]
            else:
                i -= 1

    def binarySearch(self, numbers, high, num):
        low = 0
        while high >= low:
                mid = (high + low) // 2
                if num == numbers[mid]:
                    return mid
                elif num < numbers[mid]:
                    high = mid - 1
                elif num > numbers[mid]:
                    low = mid + 1
        return -1

s = Solution()
print(s.twoSum([2,7,11,15], 9))
