import sys
import heapq

V, E=map(int, sys.stdin.readline().split())
K=int(sys.stdin.readline())
dist=[sys.maxsize for _ in range(V+1)]
graph=[[] for _ in range(V+1)]

for _ in range(E):
    s,e,c=map(int, sys.stdin.readline().split())
    graph[s].append([e,c])

heap=[]
heapq.heappush(heap,(0,K))
dist[K]=0

while heap:
    cost,v=heapq.heappop(heap)
    for e, weight in graph[v]:
        if dist[e]>cost+weight:
            dist[e]=cost+weight
            heapq.heappush(heap,(dist[e],e))

for c in dist[1:]:
    print(c if c!=sys.maxsize else "INF")