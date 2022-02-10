import sys
from collections import deque
T=int(sys.stdin.readline())

for _ in range(T):
    airports, total_cost, tickets =map(int, sys.stdin.readline().split())
    information=[[] for _ in range(airports+1)]
    for _ in range(tickets):
        u,v,c,d=map(int,sys.stdin.readline().split())
        information[u].append([v,c,d])
    result=[[sys.maxsize for _ in range(total_cost+1)] for _ in range(airports+1)]
    start=1
    result[1][0]=0

    for money in range(total_cost+1):
        for vertex in range(1,airports+1):
            if result[vertex][money]>=sys.maxsize:
                continue
            for dest, cost, dist in information[vertex]:
                if money+cost<=total_cost and dist+result[vertex][money]<result[dest][money+cost]:
                    result[dest][money+cost]=dist+result[vertex][money]


    print(min(result[airports]) if min(result[airports])<sys.maxsize else "Poor KCM")