from collections import Counter

def solution(n):
    answer = n+1
    while Counter(bin(n)[2:])['1'] != Counter(bin(answer)[2:])['1']:
        answer += 1
    return answer
