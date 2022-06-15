def solution(n, computers):
    answer = 0
    network = {i:set([]) for i in range(n)}
    for idx1, computer in enumerate(computers):
        for idx2, adj in enumerate(computer):
            if adj == 1:
                network[idx1].add(idx2)

    for node in network:
        for adj in network[node]:
            network[adj] |= network[node]
    net_set = set([])
    
    for sub_set in network.values():
        if not net_set & sub_set:
            print(net_set, sub_set)
            answer += 1
        net_set |= sub_set
        
    return answer
