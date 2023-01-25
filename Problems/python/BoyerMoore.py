#!/usr/bin/env python3

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        count = 0
        for num in nums:
            if count == 0:
                candidate = num
                count = 1
            elif num == candidate:
                count += 1
            else:
                count -= 1
        return candidate
"""
This solution uses the "Boyer-Moore Voting Algorithm", which works by maintaining a current candidate and a counter.
The algorithm iterates through the list, and for each element, it checks whether the counter is 0. If it is, the element becomes the new candidate.
If the element is the same as the candidate, the counter is incremented, otherwise, it is decremented.
At the end of the iteration, the candidate is returned as the majority element.
Because the algorithm maintains a count of the majority element, it is guaranteed that the majority element will be the final candidate.
This solution has a linear time complexity, O(n), because it iterates through the list once
and a space complexity of O(1) because it only uses a constant number of variables.
"""
