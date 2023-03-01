#!/usr/bin/env python3

class Solution:
    def findTheArrayConcVal(self, nums: list[int]) -> int:
        if not nums:
            return 0
        sum = 0
        i = 0
        j = len(nums) - 1
        while i <= j:
            if i != j:
                conc = str(nums[i]) + str(nums[j])
            else:
                conc = str(nums[i])
            # print(conc)
            sum += int(conc)
            i += 1
            j -= 1
        return sum
s = Solution()
print(s.findTheArrayConcVal([1]))
