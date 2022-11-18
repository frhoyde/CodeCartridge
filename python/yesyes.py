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
str1 = ''
while t:
    t-=1
    str1 = str(input()).strip()
    givenStr = "Yes"*20
    if str1 in givenStr:
        print("Yes")
    else:
        print("No")
