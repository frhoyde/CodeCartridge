#!/usr/bin/env python3


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

while t:
    t -= 1
    c = str(input())
    # print(c)
    if c[0] in "codeforces":
        print("YES")
    else:
        print("NO")
