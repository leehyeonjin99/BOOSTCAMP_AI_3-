from collections import deque
def solution(n):
    res = [[0]*n for _ in range(n)]
    answer = []
    x, y = -1, 0
    num = 1
    
    for i in range(n):
        for j in range(i, n):
            if i%3 == 0: # 아래로
                x += 1
            elif i%3 == 1: # 오른쪽
                y += 1
            else:
                x -= 1
                y -= 1
            res[x][y] = num
            num += 1

    for i in range(n):
        answer += res[i][:i+1]
        
    return answer