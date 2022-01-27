import sys
import heapq

V, E=map(int, sys.stdin.readline().split())
K=int(sys.stdin.readline())
K=K-1
dist=[sys.maxsize for _ in range(V)]
# 메모리 초과 : graph=[[sys.maxsize for _ in range(V)] for __ in range(V)]
# 인접 리스트 사용
graph=[[] for _ in range(V)]

for _ in range(E):
    s,e,c=map(int, sys.stdin.readline().split())
    s=s-1
    e=e-1
    graph[s].append([e,c])

heap=[]
heapq.heappush(heap,(0,K))
dist[K]=0

while heap:
    cost,v=heapq.heappop(heap)
    for end in graph[v]:
        e=end[0]
        weight=end[1]
        if dist[e]>cost+weight:
            dist[e]=cost+weight
            heapq.heappush(heap,(dist[e],e))

for c in dist:
    if c==sys.maxsize:
        print('INF')
    else:
        print(c)