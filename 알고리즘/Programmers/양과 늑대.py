from collections import deque

def solution(info, edges):
    answer = 0
    tree = {i: [] for i in range(len(info))}
    for edge in edges:
        tree[edge[0]].append(edge[1])
    
    sheep = (info[0] == 0)
    if sheep:
        que = deque([[0, [1, 0], set(tree[0])]])
    else:
        return 0
    
    while que:
        now_node, now_sw, next_nodes = que.popleft()
        # print("="*5, now_node, now_sw, "="*5)
        answer = max(answer, now_sw[0])
        for next_node in next_nodes:
            # print(next_node, info[next_node])
            if info[next_node]==1 and now_sw[0] == now_sw[1] + 1:
                # print("sheep is eaten")
                continue
            elif info[next_node]==1:
                next_sw = [now_sw[0], now_sw[1]+1]
            else:
                next_sw = [now_sw[0]+1, now_sw[1]]
            
            tmp_next_nodes = next_nodes.copy()
            tmp_next_nodes.remove(next_node)
            tmp_next_nodes.update(tree[next_node])
            # print(next_nodes, tmp_next_nodes)
            que.append([next_node, next_sw, tmp_next_nodes])
    
    return answer
