#!/usr/bin/env python3

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        distinct = set()
        for i in nums:
                distinct.add(i)
        if len(distinct) == len(nums):
            return False
        else:
            return True
# Set is used here because set automatically does not add duplicates and has a O(1) for the "in" Keyword because it is a hash table.
