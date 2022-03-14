def div(num):
    result = ''
    while num >= 1:
        result += str(num % 3)
        if num % 3 == 0:
            num = num //3 -1
        else:
            num = num // 3
    result = result.replace('0' , '4')
    return result[-1::-1]

def solution(n):
    answer = div(n)
    return answer