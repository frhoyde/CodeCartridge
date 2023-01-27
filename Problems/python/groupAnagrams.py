#!/usr/bin/env python3

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        count = {}
        for i in strs:
            sortedWord = ''.join(sorted(i))
            # print(sortedWord)
            if sortedWord not in count:
                count[sortedWord] = [i]
            else:
                count[sortedWord].append(i)
        return count.values()



s = Solution()
print(s.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
