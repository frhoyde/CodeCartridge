#!/usr/bin/env python3
# Problem Statement https://leetcode.com/problems/toeplitz-matrix/

class Solution:
    def isToeplitzMatrix(self, matrix: list[list[int]]) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        flag = True
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] != matrix[i-1][j-1]:
                    flag = False
                    print(flag)
        if flag:
            print("true")
        else:
            print("false")



sol = Solution()
sol.isToeplitzMatrix([[1,2,3,4],[5,1,2,3],[9,5,1,2]])
