#!/usr/bin/env python3

class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        num = self.arrToInt(digits)
        num += 1
        return self.intToArray(num)

    def arrToInt(self, arr):
        sum = 0
        x = len(arr) - 1
        for i in arr:
            sum += i * (10**x)
            x -= 1
        return sum
    def intToArray(self, N):
        arr = []
        while N != 0:
            arr.append(N%10)
            N = N//10
        return arr[::-1]






s = Solution()
print(s.plusOne([9]))
