import sys
N=int(sys.stdin.readline())
A=list(map(int,sys.stdin.readline().split()))
M=int(sys.stdin.readline())
B=list(map(int,sys.stdin.readline().split()))

dict={}
for num in A:
    if num in dict.keys():
        dict[num]+=1
    else:
        dict[num]=1

for num in B:
    if num in dict:
        print(dict[num], end=' ')
    else:
        print(0, end=' ')

'''for num in B:
    left, right=0,N-1
    while True:
        if left>right:
            print(0, end=' ')
            break
        mid=(left+right)//2
        if A[mid]==num:
            count=1
            i,j=1,1
            while mid-i>=0 and A[mid-i]==num:
                count+=1
                i+=1
            while mid+j<N and A[mid+j]==num:
                count+=1
                j+=1
            print(count, end=' ')
            break
        elif A[mid]<num:
            left=mid+1
        else:
            right=mid-1'''