def solution(rows, columns, queries):
    answer = []
    matrix = [[j * columns + i + 1 for i in range(columns)] for j in range(rows)]
    print(len(matrix))
    for query in queries:
        x1, y1, x2, y2 = query
        x1, y1, x2, y2 = x1 - 1, y1 - 1, x2 - 1, y2 - 1
        temp = matrix[x1][y1]
        numbers = [temp]
        for j in range(y1+1, y2+1):
            temp, matrix[x1][j] = matrix[x1][j], temp
            numbers.append(temp)
        for i in range(x1+1, x2+1):
            temp, matrix[i][y2] = matrix[i][y2], temp
            numbers.append(temp)
        for j in range(y2-1, y1-1, -1):
            temp, matrix[x2][j] = matrix[x2][j], temp
            numbers.append(temp)
        for i in range(x2-1, x1-1, -1):
            temp, matrix[i][y1] = matrix[i][y1], temp
            numbers.append(temp)
        answer.append(min(numbers))
    return answer