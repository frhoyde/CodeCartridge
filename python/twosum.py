# Problem Statement https://leetcode.com/problems/two-sum/


class Solution:
    def twoSum (self, nums: list[int], target: int) -> list[int]:
        seen_dict = {}
        for i, val in enumerate(nums):
            rem = target - nums[i]
            if rem in seen_dict:
                return [i, seen_dict[rem]]
            else:
                seen_dict[val] = i


Sol = Solution();
print(Sol.twoSum([3,3],6))

# if rem (lets say 2) is not already in seen_dict then the val(lets say 1) is stored in seen_dict becuase, if rem(2) exists in nums then the loop will find (2) as val and look for (1) as rem which is stored in seen_dict
