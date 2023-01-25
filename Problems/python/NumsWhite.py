import sys
from sys import stdin, stdout
input = stdin.readline
output = stdout.write

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
    n = inp()
    nums = []
    nums = [i for i in range(1, n+1)]
    print(2)
    while len(nums) > 1:
        a = nums[n-1]
        b = nums[n-2]
        c = (int)((a+b+1)/2)
        nums.remove(a)
        nums.remove(b)
        nums.append(c)
        nums.sort()
        n -= 1
        output(f'{a} {b}' + "\n")
