import sys
from collections import deque
N,M=map(int,sys.stdin.readline().split())
board=[]
for _ in range(N):
    board.append(list(map(int,(' '.join(sys.stdin.readline()).split()))))

visited=[]
dist=[[sys.maxsize for _ in range(M)] for _ in range(N)]
dist[0][0]=1
que=deque([[[0,0],1]])

def check_wall(index):
    return bool(board[index[0]][index[1]])

while que:
    index,hammer=que.popleft()
    if index not in visited:
        visited.append(index)
        next_index=[]
        if index[0]>0:
            wall=check_wall([index[0]-1,index[1]])
            if wall:
                if hammer:
                    next_index.append([[index[0]-1,index[1]],hammer-1])
            else:
                next_index.append([[index[0]-1,index[1]],hammer])        
        if index[0]<N-1:
            wall=check_wall([index[0]+1,index[1]])
            if wall:
                if hammer:
                    next_index.append([[index[0]+1,index[1]],hammer-1])
            else:
                next_index.append([[index[0]+1,index[1]],hammer])
        if index[1]>0:
            wall=check_wall([index[0],index[1]-1])
            if wall:
                if hammer:
                    next_index.append([[index[0],index[1]-1],hammer-1])
            else:
                next_index.append([[index[0],index[1]-1],hammer])
                
        if index[1]<M-1:
            wall=check_wall([index[0],index[1]+1])
            if wall:
                if hammer:
                    next_index.append([[index[0],index[1]+1],hammer-1])
            else:
                next_index.append([[index[0],index[1]+1],hammer])

        for next, next_hammer in next_index:
            if next not in visited:
                dist[next[0]][next[1]]=dist[index[0]][index[1]]+1
                que.append([next,next_hammer])

print(dist[N-1][M-1] if dist[N-1][M-1]<sys.maxsize else -1)