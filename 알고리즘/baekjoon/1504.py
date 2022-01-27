import sys
import heapq

N,E=map(int,sys.stdin.readline().split())
graph=[[] for _ in range(N+1)]
for _ in range(E):
    s,e,w=map(int,sys.stdin.readline().split())
    graph[s].append([e,w])
    graph[e].append([s,w])

point1,point2=map(int,sys.stdin.readline().split())
def dijkstra(start):
    dist=[sys.maxsize for _ in range(N+1)]
    heap=[]
    heapq.heappush(heap,[0, start])
    dist[start]=0

    while heap:
        cost,point=heapq.heappop(heap)
        for next_point, next_cost in graph[point]:
            if cost+next_cost<dist[next_point]:
                dist[next_point]=cost+next_cost
                heapq.heappush(heap,[dist[next_point],next_point])
    return dist

start=dijkstra(1)
start_point1=dijkstra(point1)
start_point2=dijkstra(point2)
s_1_2_e=min(start[point1]+start_point1[point2]+start_point2[N],start[point2]+start_point2[point1]+start_point1[N])
print(s_1_2_e if s_1_2_e<sys.maxsize else -1)