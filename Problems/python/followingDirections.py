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
    x = y = 0
    flag = True
    dict = {
        'L': lambda x, y: (x-1,y),
        'R': lambda x, y: (x+1,y),
        'U': lambda x, y: (x, y+1),
        'D': lambda x, y: (x, y-1)
    }
    python_hehe = inp()
    s = ""
    s = input()
    for i in s[:len(s)-1]:
        x,y = dict[i](x, y)
        if x == 1 and y == 1:
            print("YES")
            flag = False
            break
    if flag:
        print("NO")
