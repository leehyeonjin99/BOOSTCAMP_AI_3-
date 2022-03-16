'''
정확도 : 16/16
효율성 : 0/5
from collections import deque
def solution(scoville, K):
    answer = 0
    scoville.sort()
    while min(scoville) < K :
        m1 = scoville[0]
        m2 = scoville[1]
        scoville = scoville[2:]
        scoville.append(m1 + 2 * m2)
        scoville.sort()
        answer += 1
        if len(scoville) == 1:
            return -1 if min(scoville) < K else answer
    return answer
'''

import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while scoville[0] < K: # heapq는 자동으로 정렬이 된다. 따라서, socville[0] == min(scoville)
        if len(scoville) == 1:
            return -1
        m1 = heapq.heappop(scoville)
        m2 = heapq.heappop(scoville)
        heapq.heappush(scoville, m1 + 2 * m2)
        answer += 1
    return answer