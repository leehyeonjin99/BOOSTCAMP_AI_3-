import sys
from collections import deque
def bfs():
    result=deque([start])
    while result:
        n=result.popleft()
        if n==brother:
            print(dist[n])
            return
        for next in [n-1,n+1,n*2]:
            if 0<=next<=10**5 and not dist[next] :
                dist[next]=dist[n]+1
                result.append(next)

start,brother=map(int,sys.stdin.readline().split())
dist=[0 for _ in range(10**5+1)]
bfs()