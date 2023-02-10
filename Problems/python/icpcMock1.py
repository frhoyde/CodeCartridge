# #!/usr/bin/env python3

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

while(t):
    t -= 1
    n = inp()
    scores = inlt()
    penCount = [1 for i in range(n)]
    penOwner = [i for i in range(0, n)]
    q = inp()
    while(q):
        print(penCount, penOwner, scores)
        q -= 1
        qin = inlt()
        if(qin[0] == 1):
            p1 = qin[1] - 1
            p2 = qin[2] - 1
            if penCount[p1] == 0 or penCount[p2] == 0:
                continue
            elif scores[p1] > scores[p2]:
                scores[p1] += scores[p2]
                penOwner = [p1 if i == p2 else i for i in penOwner]
                penCount[p1] += penCount[p2]
                penCount[p2] = 0
                scores[p2] = 0
            elif scores[p1] < scores[p2]:
                scores[p2] += scores[p1]
                penOwner = [p2 if i == p1 else i for i in penOwner]
                penCount[p2] += penCount[p1]
                penCount[p1] = 0
                scores[p1] = 0
        elif(qin[0] == 2):
            p = qin[1] - 1
            print(penCount[p])
        elif(qin[0] == 3):
            p = qin[1] - 1
            print(penOwner[p]+1)
