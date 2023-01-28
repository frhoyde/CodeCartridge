#!/usr/bin/env python3
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = []
        s = s.lower()
        for i in s:
            if ord(i) in range(ord("a"), ord("z")+1) or ord(i) in range(ord("0"), ord("9")+1):
                s1.append(i)
        if len(s) <= 1:
            return True
        for i,j in zip(range(len(s1)), range(len(s1)-1, -1, -1)):
            if i >= j:
                break
            if s1[i] != s1[j]:
                return False

        return True


s = Solution()
print(s.isPalindrome("race a car"))
print(s.isPalindrome("A man, a plan, a canal: Panama"))
print(s.isPalindrome("0P"))
