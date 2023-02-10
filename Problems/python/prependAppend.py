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
    python_hehe = inp()
    s = input()
    s = insr()
    count1 = 0
    count2 = 0
    flag1 = True
    flag2 = True
    for i, j in zip(range(0, python_hehe), range(python_hehe, -1, -1)):
        var1 = s[0]
        var2 = s[len(s)-1]
        if(s[i] == var1 and flag1):
            count1 += 1
        else:
            flag1 = False
        if(s[j] == var2 and flag2):
            count2 += 1
        else:
            flag2 = False
        if (not flag1 and not flag2):
            break
        print(python_hehe - count1 - count2 + 2)
