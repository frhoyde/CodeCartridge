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
    t-=1
    m, s = inlt()
    foundNums = inlt()
    sumFoundNums = sum(foundNums)
    maxFoundNum = max(foundNums)
    sumNatural = int((maxFoundNum * (maxFoundNum + 1))/2)
    diffSum = sumNatural - sumFoundNums
    if s < diffSum:
        print("No")
    elif s == diffSum:
        print("Yes")
    else:
        s -= diffSum
        maxFoundNum += 1
        while True:
            if s < maxFoundNum:
                print("No")
                break;
            elif s == maxFoundNum:
                print("Yes")
                break;
            else:
                s -= maxFoundNum
                maxFoundNum += 1
