from collections import deque

def solution(n, wires):
    answer = n
    tree = [[] for _ in range(n+1)]
    for a, b in wires:
        tree[a].append(b)
        tree[b].append(a)
    for wire in wires:
        visited1 = [0 for _ in range(n+1)]
        que1 = deque([wire[0]])
        while que1:
            next_node = que1.popleft()
            if next_node == wire[1]:
                continue
            if not visited1[next_node]:
                visited1[next_node] = 1
                que1 += tree[next_node]
        diff = abs(2 * sum(visited1) - n)
        if diff < answer:
            answer = diff
        
    return answer
