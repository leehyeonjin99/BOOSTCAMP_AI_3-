from math import factorial
def solution(n, k):
    answer = []
    people = list(range(1, n+1))
    total = factorial(n-1)
    for col in range(n-1, 0, -1):
        # print(people)
        p = k // total
        r = k % total
        # print(total, p, r)
        if r == 0:
            answer.append(people[p-1])
            people = people[:p-1] + people[p:]
            answer += people[::-1]
            break
        else:
            answer.append(people[p])
            people = people[:p] + people[p+1:]
            if r == 1:
                answer += people[:]
                break
        k = r
        total = total // col
    return answer
