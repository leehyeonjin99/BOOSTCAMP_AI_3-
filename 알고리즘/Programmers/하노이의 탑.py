def hanoi(num, start, end, middle):
    if num == 1:
        return [[start,end]]
    else:
        return hanoi(num-1, start, middle, end) + [[start,end]] + hanoi(num-1, middle, end, start)
    
def solution(n):
    return hanoi(n, 1, 3, 2)
