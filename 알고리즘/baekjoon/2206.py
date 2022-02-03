import sys
from collections import deque

d=[0,0,1,-1]

N,M=map(int,sys.stdin.readline().split())
board=[]
for _ in range(N):
    board.append(list(map(int,(' '.join(sys.stdin.readline()).split()))))

visited=[[[0 for _ in range(M)] for _ in range(N)] for _ in range(2)]
visited[1][0][0]=1
que=deque([[0,0,1]])
def dfs():
    while que:
        x,y,hammer=que.popleft()

        if x==N-1 and y==M-1:
            print(visited[hammer][x][y])
            return

        for i in range(4):
            next_x=x+d[i]
            next_y=y+d[3-i]

            if 0<=next_x<N and 0<=next_y<M:
                if board[next_x][next_y]==1 and hammer==1:
                    visited[0][next_x][next_y]=visited[hammer][x][y]+1
                    que.append([next_x,next_y,0])
                elif board[next_x][next_y]==0 and visited[hammer][next_x][next_y]==0:
                    visited[hammer][next_x][next_y]=visited[hammer][x][y]+1
                    que.append([next_x,next_y,hammer])  
    print(-1)
    return

dfs()