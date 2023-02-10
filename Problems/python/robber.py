#!/usr/bin/env python3

class Solution:
    def minCapability(self, nums: list[int], k: int) -> int:
        arr = []
        for i in range(len(nums)):
            k2 = 0
            maxSteal = 0
            for j in range(i, len(nums), 2):
                if maxSteal < nums[j]:
                    maxSteal = nums[j]
                k2 += 1
            if k2 >= k:
                arr.append(maxSteal)
        print(arr)
        return min(arr)


s = Solution()
print(s.minCapability([2,3,5,9], 2))
print(s.minCapability([2,7,9,3,1], 2))
# this can be solved via sliding window approach please solve it it is not solved yet
