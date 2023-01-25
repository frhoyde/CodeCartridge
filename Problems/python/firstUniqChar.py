#!/usr/bin/env python3

class Solution:
    def firstUniqChar(self, s: str) -> int:
        countChar = [0 for i in range(26)]
        for i in s:
            countChar[ord(i) - ord('a')] += 1
        for i, element in enumerate(s):
            if countChar[ord(element) - ord('a')] < 2:
                return i
        return -1
