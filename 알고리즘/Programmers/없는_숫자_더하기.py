def solution(numbers):
    L = [i for i in range(10)]
    for num in numbers:
        L.remove(num)
    return sum(L)

'''
# shorcode
solution = lambda x : 45-sum(x)
'''