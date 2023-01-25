#!/usr/bin/env python3
# Problem Statement https://leetcode.com/problems/palindrome-number/
class Solution:
    def isPalindrome(self, x: int) -> bool:
        numStr = str(x)
        strLen = len(numStr)
        for i in range(0, int(strLen/2)+1):
            subStr1 = numStr[:i]
            subStr2 = numStr[strLen - i:]
            subStr2 = subStr2[::-1]
            if subStr1 != subStr2:
                return 0
        return 1

Sol = Solution()
Sol.isPalindrome(12344321)
