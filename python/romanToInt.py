#!/usr/bin/env python3

class Solution:
    def romanToInt(self, s: str) -> int:
        values = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        num = 0
        for i in range(len(s)-1, -1, -1):
            if i > 0 and (values[s[i]] > values[s[i-1]]):
                num += values[s[i]] - 2* values[s[i-1]]
            else:
                num += values[s[i]]
            # print(num)
        return num

s = Solution()
print(s.romanToInt("XIV"))
