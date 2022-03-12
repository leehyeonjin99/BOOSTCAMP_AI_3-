def division(num, div):
    result = ''
    if num == 0:
        return list('0')
    while num>0:
        a = num % div
        if a>=10:
            a = chr(a+ord('A')-10)
        result+=str(a)
        num = num // div
    return list(result[::-1])

def solution(n, t, m, p):
    answer = ''
    L = []
    num = 0
    while len(L) < t * m:
        L+=division(num, n)
        num+=1
    answer=''.join(L[p-1::m][:t])
    return answer