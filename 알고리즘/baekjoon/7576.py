import sys

M,N=map(int,sys.stdin.readline().split())
board=[]
for _ in range(N):
    board.append(list(map(int,sys.stdin.readline().split())))
dist=[[0 for _ in range(M)] for _ in range(N)]

from collections import deque
que=deque([])
for i in range(N):
    for j in range(M):
        if board[i][j]==1:
            que.append([i,j])
        if board[i][j]==-1:
            dist[i][j]=-1

count=0
while que:

    if all(0 not in l for l in dist):
        break

    index=que.popleft()
    i=index[0]
    j=index[1]
    next=[]
    if i>0:
        next.append([i-1,j])
    if i<N-1:
        next.append([i+1,j])
    if j>0:
        next.append([i,j-1])
    if j<M-1:
        next.append([i,j+1])

    for n in next:
        next_i=n[0]
        next_j=n[1]
        if board[next_i][next_j]==0 and not dist[next_i][next_j]:
            dist[next_i][next_j]=dist[i][j]+1
            que.append([next_i,next_j])
    count+=1

check=True

for i in range(N):
    for j in range(M):
        if board[i][j]==0 and dist[i][j]==0:
            check=False

print(max(map(max,dist)) if check else -1)