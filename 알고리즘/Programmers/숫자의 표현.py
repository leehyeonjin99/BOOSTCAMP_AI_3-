def solution(n):
    answer = 0
    count = 0
    sum = 0
    while True:
        if (n - sum) // (count + 1) < 1:
            return answer
        if (n - sum) % (count + 1) == 0:
            answer += 1
        sum += count+1
        count += 1
    return answer
