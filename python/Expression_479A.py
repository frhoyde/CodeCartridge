# Problem statement https://codeforces.com/problemset/problem/479/A
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

a = inp()
b = inp()
c = inp()
ans = a + b + c
ans = max(ans, a * b * c)
ans = max(ans, (a+b) * c)
ans = max(ans, a* (b+c))
print(ans)
