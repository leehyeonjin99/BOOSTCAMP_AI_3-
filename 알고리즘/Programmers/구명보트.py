from collections import deque

def solution(people, limit):
    answer = 0
    people.sort()
    que = deque(people)
    '''
    시간초과
    while que:
        now = que.popleft()
        small = 300
        for q in que:
            if q+now <= limit:
                small = q
                continue
        if small!=300:
            que.remove(small)
        answer += 1
    '''
    while que:
        if len(que) == 1:
            que.pop()
            answer += 1
        elif que[0] + que[-1] <= limit:
            answer += 1
            que.pop()
            que.popleft()
        else:
            que.pop()
            answer += 1
    return answer
