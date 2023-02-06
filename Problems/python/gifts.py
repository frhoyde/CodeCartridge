#!/usr/bin/env python3
import math
class Solution:
    def pickGifts(self, gifts: list[int], k: int) -> int:
        maxgift = 0
        gifts = sorted(gifts, reverse=True)
        k2 = 0
        sum = 0
        # print(gifts)
        while(k2 < k):
            k2 += 1
            gifts[0] = math.floor(gifts[0] ** 0.5)
            gifts = sorted(gifts, reverse=True)
        for i in gifts:
            sum += i
        return sum



s = Solution()
print(s.pickGifts([25,64,9,4,100], 4))
print(s.pickGifts([1,1,1,1], 4))
