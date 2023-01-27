#!/usr/bin/env python3

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        j = 1
        maxdiff = 0
        while j < len(prices):
            if (prices[i] > prices[j]):
                i = j
                j += 1
                continue
            else:
                diff = prices[j] - prices[i]
                maxdiff = max(diff, maxdiff)
                j += 1
        return maxdiff
