from math import factorial as F

def solution(n):
    answer = [1 for _ in range(n+1)]
    for i in range(2, n+1):
        answer[i] = answer[i-1] + answer[i-2]
    return answer[n] % 1234567
