import sys
import heapq

def Bellman(start):
    dist=[sys.maxsize for _ in range(n+1)]
    heap=[]
    heapq.heappush(heap,([start,0]))
    dist[start]=0
    while heap:
        s,d=heapq.heappop(heap)
        for next in graph[s]:
            next_dist=d+next[1]
            if dist[next[0]]>next_dist:
                dist[next[0]]=next_dist
                heapq.heappush(heap,(next[0],next_dist))
    return dist

T=int(sys.stdin.readline())
for i in range(T):
    n,m,t=map(int,sys.stdin.readline().split())
    s,g,h=map(int,sys.stdin.readline().split())
    graph={i:[] for i in range(1,n+1)}
    for _ in range(m):
        a,b,c=map(int, sys.stdin.readline().split())
        graph[a].append([b,c])
        graph[b].append([a,c])
    subs=[]
    for _ in range(t):
        subs.append(int(sys.stdin.readline()))
    dist_start=Bellman(s)
    dist_h=Bellman(h)
    dist_g=Bellman(g)
    result=[]

    for sub in subs:
        check1=(dist_start[sub]==dist_start[h]+dist_h[g]+dist_g[sub])
        check2=(dist_start[sub]==dist_start[g]+dist_g[h]+dist_h[sub])
        if check1 or check2:
            result.append(sub)
    
    result.sort()
    for r in result:
        print(r, end=' ')
    print()

