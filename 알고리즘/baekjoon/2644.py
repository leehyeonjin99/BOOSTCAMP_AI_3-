import sys
N=int(sys.stdin.readline())
a,b=map(int, sys.stdin.readline().split())
M=int(sys.stdin.readline())
L={}
for _ in range(M):
    x, y=map(int,sys.stdin.readline().split())
    if x in L:
        L[x].append(y)
    else:
        L[x]=[y]
    if y in L:
        L[y].append(x)
    else:
        L[y]=[x]

from collections import deque
dist=[-1 for _ in range(N+1)]
que=deque([a])
dist[a]=0

while que:
    now=que.popleft()
    for next in L[now]:
        if dist[next]==-1:
            que.append(next)
            dist[next]=dist[now]+1

print(dist[b])
        