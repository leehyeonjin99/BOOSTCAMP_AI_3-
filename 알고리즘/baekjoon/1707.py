import sys
from collections import deque
sys.setrecursionlimit(10 ** 6)

def solution(start, group):
    visited[start]=group
    for v in graph[start]:
        if visited[v]==0:
            if not solution(v, -group):
                return False
        elif visited[v]==visited[start]:
            return False
    return True

K=int(sys.stdin.readline())
for _ in range(K):
    V,E=map(int, sys.stdin.readline().split())
    graph=[[] for _ in range(V+1)]
    for _ in range(E):
        u,v=map(int,sys.stdin.readline().split())
        graph[u].append(v)
        graph[v].append(u)
    visited=[0 for _ in range(V+1)]
    for start in range(1,V+1):
        if visited[start]==0:
            result=solution(start,1)
            if not result:
                break
    print("YES" if result else "NO")
