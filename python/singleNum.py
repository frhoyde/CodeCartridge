#!/usr/bin/env python3

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums) == 1 or (nums[-1] != nums[-2]):
            return nums[-1]
        for i in range(0,len(nums)-2, 2):
            if nums[i] != nums[i+1]:
                return nums[i]
        return -1
