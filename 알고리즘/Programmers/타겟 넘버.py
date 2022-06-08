from collections import deque

def solution(numbers, target):
    answer = 0
    result_count = deque([[0, 0]])
    while result_count:
        now_result, now_count = result_count.popleft()
        if now_count == len(numbers):
            if now_result == target:
                answer += 1
        else:
            for next_num in [+numbers[now_count], -numbers[now_count]]:
                next_result = now_result + next_num
                next_count = now_count + 1
                result_count.append([next_result, next_count])
    return answer
