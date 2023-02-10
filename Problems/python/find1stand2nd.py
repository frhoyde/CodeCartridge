#!/usr/bin/env python3

class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        if len(nums) == 0:
            return [-1, -1]
        tmp = int(self.binarySearch(nums, target))
        if tmp == -1:
            return [-1, -1]
        start = tmp
        while nums[tmp] == nums[start]:
            start -= 1
        end = tmp
        while nums[tmp] == nums[end]:
            end += 1
        return [start+1, end-1]



    def binarySearch(self, nums, target):
        high = len(nums) - 1
        low = 0
        while high >= low:
            mid = (high + low) // 2
            if nums[mid] == target:
                return mid
            elif target <= nums[mid]:
                high = mid - 1
            elif target <= nums[high]:
                low = mid + 1
            else:
                break

        return -1

s = Solution()
# print(s.searchRange([5,7,7,8,8,10], 8))
# print(s.searchRange([5,7,7,8,8,10], 6))
# print(s.searchRange([], 0))
# print(s.binarySearch([5,7,7,8,8,10], 6))
print(s.binarySearch([2,2], 3))
