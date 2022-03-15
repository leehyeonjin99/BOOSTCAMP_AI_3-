from collections import deque
import math
def solution(progresses, speeds):
    answer = []
    days = deque([math.ceil((100-progresses[i])/speeds[i]) for i in range(len(progresses))])
    print(days)
    count, M = 1, days.popleft()
    while days:
        day = days.popleft()
        if day <= M :
            count +=1
        else :
            M = day
            answer.append(count)
            count = 1
    answer.append(count)
    return answer