#!/usr/bin/env python3
from collections import Counter
class Solution:
    def intersect(self, nums1, nums2):
        if len(nums1) > len(nums2):
            self.intersect(nums2, nums1)

        countNums1 = Counter(nums1)
        arr = []
        for i in nums2:
            if(countNums1[i] > 0):
                arr.append(i)
                countNums1[i] -= 1
        return arr



s = Solution()
print(s.intersect([1,2,2,1], [2,2]))
