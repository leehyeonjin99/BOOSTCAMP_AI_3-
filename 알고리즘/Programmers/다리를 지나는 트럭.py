from collections import deque
def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = deque([0 for _ in range(bridge_length)])
    idx = 0
    weight_sum = 0
    while bridge:
        time += 1
        out_weight = bridge.popleft()
        weight_sum -= out_weight
        if idx < len(truck_weights):
            if weight_sum + truck_weights[idx] <= weight:
                weight_sum += truck_weights[idx]
                bridge.append(truck_weights[idx])
                idx += 1
            else:
                bridge.append(0)
    return time
