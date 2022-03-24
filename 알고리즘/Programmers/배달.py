from collections import deque

def solution(N, road, K):
    answer = 0
    
    map = {}
    for r in road:
        start = r[0]
        end = r[1]
        cost = r[2]
        if start in map:
            map[start].append([end, cost])
        else:
            map[start] = [[end, cost]]
        if end in map:
            map[end].append([start, cost])
        else:
            map[end] = [[start, cost]]
    cost = [10000*50 for _ in range(N+1)]
    cost[1] = 0
    que = deque([1])
    while que:
        vertex = que.popleft()
        for next_vertex, next_cost in map[vertex]:
            if cost[next_vertex] > cost[vertex] + next_cost:
                que.append(next_vertex)
                cost[next_vertex] = cost[vertex] + next_cost
    
    for c in cost:
        if c<=K:
            answer+=1
        
    return answer
