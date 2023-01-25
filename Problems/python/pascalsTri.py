#!/usr/bin/env python3

class Solution:
    factorial = [-1 for k in range(0, 31)]
    def generate(self, numRows: int):
        triangle = []
        triangle.append([1])
        if(numRows == 1):
            return triangle
        numRows -= 1
        while numRows >= 1:
            row = []
            for i in range(0, numRows+1):
                row.append(self.nCr(numRows, i))
            triangle.insert(1, row)
            numRows -= 1
        return triangle

    def fact(self, n):
        if(n == 1 or n == 0):
            self.factorial[n] = 1
        if self.factorial[n] != -1:
            return self.factorial[n]
        else:
            self.factorial[n] = n * self.fact(n-1)
            return self.factorial[n]
    def nCr(self, n, r):
        return (int)(self.fact(n)/(self.fact(n-r)*self.fact(r)))


s = Solution()
print(s.generate(6))
