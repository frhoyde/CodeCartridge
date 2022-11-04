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
    n = inp()
    flag = 1
    numOfOp = 0
    if n % 2 == 0:
        numOfOp = int(n/2)
        flag = 0
    elif n == 1:
        numOfOp = 1
    else:
        numOfOp = int((n+1)/2)
    print(numOfOp)
    istart = 2
    jstart = 6
    if flag:
        print("1 2")
        istart = 5
        jstart = 9
        numOfOp -= 1
    for i in range(0, numOfOp):
        ik = istart + 6*i
        jk = jstart + 6*i
        print(f'{ik} {jk}')
