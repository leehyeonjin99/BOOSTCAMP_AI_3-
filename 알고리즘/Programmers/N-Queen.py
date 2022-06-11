def dfs(arr, now, end):
    answer = 0
    if now == end:
        return 1
    for new_col in range(end):
        check = True
        for row, col in enumerate(arr):
            if new_col == col or abs(new_col - col) == abs(row - now):
                check = False
                break
        if check:
            answer += dfs(arr + [new_col], now+1, end)
    return answer

def solution(n):
    answer = 0
    for col in range(n):
        answer += dfs([col], 1, n)
    return answer
