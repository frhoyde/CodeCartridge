#!/usr/bin/env python3

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 1
        currLength = 0
        if len(s) == 0:
            return 0
        subStr = s[0]
        for i in s[1:]:
            while i in subStr:
                subStr = subStr[1:]
            subStr += i
            currLength = len(subStr)
            if currLength > maxLength:
                maxLength = currLength
        return maxLength
