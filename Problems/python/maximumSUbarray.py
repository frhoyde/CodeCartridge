#!/usr/bin/env python3

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        maxSum = 0
        i = j = 0
        sum = nums[i]
        while i < len(nums):
            if j == len(nums) - 1:
                i += 1
                j = i
                sum = 0
            else:
                j += 1
                sum += nums[j]
                maxSum = max(sum, maxSum)

        return maxSum



s = Solution()
print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
