import sys
N=int(sys.stdin.readline())
A=list(map(int, sys.stdin.readline().split()))
A.sort()
M=int(sys.stdin.readline())
B=list(map(int,sys.stdin.readline().split()))

for num in B:
    left, right=0, N-1
    while 1:
        if left>right:
            print(0)
            break
        mid=(left+right)//2
        if num==A[mid]:
            print(1)
            break
        elif num<A[mid]:
            right=mid-1
        else:
            left=mid+1
        