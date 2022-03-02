import sys

N, M=map(int,sys.stdin.readline().split())
count=1

while True:
    if N==M:
        break
    elif N>M or (M%10!=1 and M%2!=0):
        count=-1
        break
    # 10으로 나눴을 때 나머지가 1인 경우와 2로 나누어 떨어지는 경우는 동시에 일어날 수 없다
    elif M%10==1:
        M=(M-1)//10
        count+=1
    elif M%2==0:
        M=M//2
        count+=1

print(count)
