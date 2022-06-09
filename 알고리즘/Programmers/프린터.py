from collections import deque
def solution(priorities, location):
    answer = 0
    print_list = deque(list(enumerate(priorities)))
    priorities.sort(reverse=True)
    max_idx = 0
    while True:
        idx, prior = print_list.popleft()
        if prior == priorities[max_idx]:
            max_idx += 1
            answer += 1
            if idx == location:
                return answer
        else:
            print_list.append((idx, prior))
    return answer
