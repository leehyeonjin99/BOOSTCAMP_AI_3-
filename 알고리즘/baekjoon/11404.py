import sys
N=int(sys.stdin.readline())
E=int(sys.stdin.readline())
graph=[[sys.maxsize for _ in range(N+1)] for _ in range(N+1)]
for i in range(E):
    s,e,c=map(int,sys.stdin.readline().split())
    graph[s][e]=min(graph[s][e],c)
dist=[[sys.maxsize for _ in range(N+1)] for _ in range(N+1)]
for i in range(1,N+1):
    for j in range(1,N+1):
        if i==j:
            graph[i][j]=0
        dist[i][j]=graph[i][j]

for k in range(1,N+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
            dist[i][j]=min(dist[i][j],dist[i][k]+dist[k][j])

for i in range(1, N+1):
    for j in range(1,N+1):
        print(dist[i][j] if dist[i][j]<sys.maxsize else 0, end=' ')
    print()