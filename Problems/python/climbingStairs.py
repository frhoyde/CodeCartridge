#!/usr/bin/env python3

class Solution:
    def climbStairs(self, n: int) -> int:
        change = [-1 for i in range(n+1)]
        change[1] = 1
        change[0] = 1
        return self.coinChange(n, change)

    def coinChange(self, n, change):
        if n < 0:
            return 0
        if change[n] == -1:
            change[n] = self.coinChange(n-1, change) + self.coinChange(n-2, change)
        return change[n]

sol = Solution()
print(sol.climbStairs(4))
