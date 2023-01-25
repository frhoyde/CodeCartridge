#!/usr/bin/env python3

class Solution:
    def isHappy(self, n: int) -> bool:
        tortoise = n
        hare = n
        while True:
            tortoise = self.digitSquareSum(tortoise)
            hare = self.digitSquareSum(hare)
            hare = self.digitSquareSum(hare)
            if hare == tortoise:
                return hare == 1

    def digitSquareSum(self, n):
        sum = 0
        temp = 0
        while n != 0:
            temp = n % 10
            sum += temp ** 2
            n = int(n/10)
        return  sum

s = Solution()
print(s.isHappy(19))
