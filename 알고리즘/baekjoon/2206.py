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

def check_wall(index):
    return bool(board[index[0]][index[1]])

while que:
    x,y,hammer=que.popleft()

    for i in range(4):
        next_x=x+d[i]
        next_y=y+d[3-i]

        if 0<=next_x<N and 0<=next_y<M:
            if check_wall([next_x,next_y]) and hammer==1:
                visited[0][next_x][next_y]=visited[hammer][x][y]+1
                que.append([next_x,next_y,0])
            elif not check_wall([next_x,next_y]) and visited[hammer][next_x][next_y]==0:
                visited[hammer][next_x][next_y]=visited[hammer][x][y]+1
                que.append([next_x,next_y,hammer])  

if visited[0][N-1][M-1]!=0 and visited[1][N-1][M-1]!=0:
    print(min(visited[0][N-1][M-1], visited[1][N-1][M-1]))
elif visited[0][N-1][M-1]!=0:
    print(visited[0][N-1][M-1])
elif visited[1][N-1][M-1]!=0:
    print(visited[1][N-1][M-1])
else:
    print(-1)