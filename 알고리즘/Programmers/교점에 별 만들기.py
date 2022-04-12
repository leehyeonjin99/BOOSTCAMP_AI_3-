def solution(line):
    intersection = []
    for i in range(len(line)):
        for j in range(i+1, len(line)):
            a, b, e = line[i]
            c, d, f = line[j]
            if a*d - b*c != 0: # 평행이 아니라면
                x, y = (b*f-e*d)/(a*d - b*c), (e*c-a*f)/(a*d - b*c)
                if x.is_integer() and y.is_integer():
                    if [int(x), int(y)] not in intersection:
                        intersection.append([int(x), int(y)])
    x_min, x_max, y_min, y_max = min(intersection)[0], max(intersection)[0], min(intersection, key = lambda x : x[1])[1], max(intersection, key = lambda x : x[1])[1]
    answer = [["." for _ in range(x_max-x_min+1)] for _ in range(y_max-y_min+1)]
    for x, y in intersection:
        print([x, y], [ abs(x-x_min), abs(y-y_min),])
        answer[(y_max-y_min) - abs(y-y_min)][abs(x-x_min)] = "*"
    for i in range(len(answer)):
        answer[i] = ''.join(answer[i])
    return answer
