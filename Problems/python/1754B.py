# Problem Statement https://codeforces.com/problemset/problem/1754/B
# Resource for greedy approach https://www.programiz.com/dsa/greedy-algorithm
import sys
input = sys.stdin.readline

############ ---- Input Functions ---- ############
def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))

t = inp()
for i in range(0, t):
    n = inp()
    nums = list(range(1, n+1))
