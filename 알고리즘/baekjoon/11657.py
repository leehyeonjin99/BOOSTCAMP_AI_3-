import sys
N,E=map(int,sys.stdin.readline().split())
INF=sys.maxsize
dist=[INF for _ in range(N+1)]
edges=[]
for _ in range(E):
    edges.append(list(map(int,sys.stdin.readline().split())))

def Bellman_Ford(start):
    dist[start]=0

    for i in range(N):
        for j in range(E):
            node=edges[j][0]
            next=edges[j][1]
            cost=edges[j][2]
            if dist[node]!=INF and dist[next]>cost+dist[node]:
                dist[next]=cost+dist[node]
                if i==N-1:
                    return True
    return False

result=Bellman_Ford(1)
if result:
    print(-1)
else:
    for d in dist[2:]:
        print(d if d<INF else -1)