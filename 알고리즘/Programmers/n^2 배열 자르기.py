def solution(n, left, right):
    arr = []
    for i in range(left//n+1, right//n+2):
        arr += [i]*i + list(range(i+1, n+1))
    arr = arr[left%n:]
    right = -(n - (right%n + 1))
    return arr if right == 0 else arr[:right]
