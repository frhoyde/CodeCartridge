#!/usr/bin/env python3

class Solution:
	def removeDuplicates(self, nums: list[int]) -> int:
		j = 0
		for i in range(1, len(nums)):
			if nums[j] != nums[i]:
				j += 1
				nums[j] = nums[i]
		return j + 1

s = Solution()
s.removeDuplicates([1,1,2])
s.removeDuplicates([0,0,1,1,1,2,2,3,3,4])
