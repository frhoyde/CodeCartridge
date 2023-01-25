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
    n = inp()
    nums = list()
    nums = inlt()
    nums.sort()
    sumArr = sum(nums)
    maxdiff = abs(sumArr)
    lowSum = 0
    for i in range(0, n):
        lowSum += nums[i]
        diff =  abs(abs(sumArr + (-1)*lowSum) - abs(lowSum))
        if(diff >= maxdiff):
            maxdiff = diff
    print(maxdiff)
