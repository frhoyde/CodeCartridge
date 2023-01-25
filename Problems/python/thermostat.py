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
    l, r, x = inlt()
    a, b = inlt()
    if(a == b):
        print(0)
        continue
    if (x >= l and x <= r):
        if abs(b-a) >= x:
            print(1)
        if (b-x) < l and (b+x) > r:
            print(-1)
        else:
            if (b-x) < l:
                if abs( a - (b+x) ) >= x:
                    print(2)
                else:
                    print(3)
            elif (b+x) > r:
                if abs( a - (b-x) ) >= x:
                    print(2)
                else:
                    print(3)
    else:
        print(-1)
