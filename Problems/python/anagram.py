#!/usr/bin/env python3

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        list = [0 for i in range(128)]
        for i in s:
            list[ord(i)-ord('a')] += 1
        for i in t:
            list[ord(i)-ord('a')] -= 1
        for i in list:
            if(i != 0):
                return False
        return True
