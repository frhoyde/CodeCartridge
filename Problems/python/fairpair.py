#!/usr/bin/env python3
class Solution:
    def countFairPairs(self, nums: list[int], lower: int, upper: int) -> int:
        nums.sort()
        start = lower
        end = lower
        count = 0
        n = len(nums)
        while nums[start] <= upper:
            print(nums[start], nums[end])
            end += 1
            if end == n:
                end = lower
            if start == end:
                continue
            count += 1
            if nums[end] > upper:
                end = lower
                start += 1
            if start == n:
                break


        return count

s = Solution()
print(s.countFairPairs([0,1,7,4,4,5], 3, 6))
