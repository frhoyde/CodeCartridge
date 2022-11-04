#!/usr/bin/env python3
# Problem Statement https://leetcode.com/problems/toeplitz-matrix/

class Solution:
    def isToeplitzMatrix(self, matrix: list[list[int]]) -> bool:
        for i,j in enumerate(matrix):
            print(i)
            print(j)
            for k in j:
                print(k)


sol = Solution()
sol.isToeplitzMatrix([[1,2,3,4],[5,1,2,3],[9,5,1,2]])
