#!/usr/bin/env python3
"""
The positive divisors of 319 are exactly the powers of 3 from 3^0 to 3^19. That's all powers of 3 in the possible range here (signed 32-bit integer). So just check whether the number is positive and whether it divides 3^19.
"""
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return n > 0 and 3**19 % n == 0
