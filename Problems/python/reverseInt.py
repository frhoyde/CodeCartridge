#!/usr/bin/env python3

class Solution:
    def reverse(self, x: int) -> int:
        isNegative = False
        if x < 0:
            isNegative = True
            x *= -1

        result = self.listToReverseInt(self.intToList(x))
        result *= (-1) if isNegative else 1
        return result if self.is_32bit(result) else 0

    def intToList(self, x):
        arr = []
        while x != 0:
            rem = x % 10
            arr.append(rem)
            x = x // 10
        return arr[-1::-1]

    def listToReverseInt(self, arr):
        num = 0
        j = 0
        for i in arr:
            num += i * (10**j)
            j += 1
        return num
    def is_32bit(self, n):
        return n >= -2**31 and n <= 2**31 - 1


s = Solution()
# print(s.intToList(1234))
# print(s.listToInt([1,2,3,4]))
# print(s.reverse(-123))
