#!/usr/bin/env python3

class Solution:
    def longestPalindrome(self, s: str) -> str:
        i = 0
        pal = s
        j = len(s)
        while i <= j or pal != "":
            k = i
            l = j
            if self.isPalindrome(pal):
                return pal
            while k < l-1:
                print(pal[k:l])
                if self.isPalindrome(pal[k:l]):
                    return pal[k:l]
                l -= 1
            l = j
            while k < l-1:
                print(pal[k:l])
                if self.isPalindrome(pal[k:l]):
                    return pal[k:l]
                k += 1
            else:
                i += 1
                j -= 1
                pal = pal[i:j]
        return s[0]

    def isPalindrome(self, s):
        if len(s) == 1:
            return True
        mid = len(s) // 2
        if len(s) % 2 == 0:
            s1 = s[0:mid]
            s2 = s[mid:]
        else:
            s1 = s[0:mid]
            s2 = s[mid+1:]
        s2 = s2[-1::-1]
        # print(s1, s2)
        return s1 == s2

s = Solution()
# print(s.isPalindrome("abba"))
print(s.longestPalindrome("eabcb"))
