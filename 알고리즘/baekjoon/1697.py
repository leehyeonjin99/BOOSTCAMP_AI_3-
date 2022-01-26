import sys
from collections import deque
def bfs(start,brother):
    visited=set()
    result=deque([start])
    while result:
        n=result.popleft()
        if n==brother:
            print(dist[n])
            return
        if n not in visited:
            visited.add(n)
            for next in [n-1,n+1,n*2]:
                if 0<=next<=10**5 and next not in visited :
                    dist[next]=dist[n]+1
                    result.append(next)

start,brother=map(int,sys.stdin.readline().split())
dist=[0 for _ in range(10**5+1)]
bfs(start,brother)