import sys
from collections import deque
def bfs(board,start):
    visited=[]
    result=deque([start])
    while result:
        n=deque.popleft(result)
        if n not in visited:
            visited.append(n)
            result+=set(board[n])-set(visited)
    return visited

N=int(sys.stdin.readline())
connect_num=int(sys.stdin.readline())
connect=[[] for _ in range(N+1)]
for _ in range(connect_num):
    a,b=map(int,sys.stdin.readline().split())
    connect[a].append(b)
    connect[b].append(a)
    result=bfs(connect,1)
print(len(result)-1)




