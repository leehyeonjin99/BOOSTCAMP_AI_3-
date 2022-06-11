def solution(triangle):
    answer = 0
    distance = []
    # print(triangle)
    for trian in triangle:
        distance.append(trian.copy())
    for col_num, row in enumerate(range(len(triangle) - 1)):
        for col in range(len(distance[row])):
            distance[row+1][col] = max(triangle[row+1][col]+distance[row][col], distance[row+1][col])
            if col < col_num+1:
                distance[row+1][col+1] = max(triangle[row+1][col+1]+distance[row][col], distance[row+1][col+1])
        # print(distance)
    return max(distance[-1])
