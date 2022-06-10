def transform(arr):
    height, width = len(arr), len(arr[0])
    T = [[0 for _ in range(height)] for _ in range(width)]
    for i in range(height):
        for j in range(width):
            T[j][i] = arr[i][j]
    return T

def mul(arr1, arr2):
    S = 0
    for i, j in zip(arr1, arr2):
        S += (i*j)
    return S

def solution(arr1, arr2):
    height, width = len(arr1), len(arr2[0])
    answer = [[0 for _ in range(width)] for _ in range(height)]
    arr2 = transform(arr2)
    for i in range(height):
        for j in range(width):
            answer[i][j] = mul(arr1[i], arr2[j])          
    return answer
