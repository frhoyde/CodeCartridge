#!/usr/bin/env python3

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        sum = 0
        columnTitle = reversed(columnTitle.lower())
        for i, j in enumerate(columnTitle):
            sum += (26 ** i) * (ord(j) - ord('a') + 1)
        return sum
