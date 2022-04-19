def solution(dirs):
    answer = 0
    dist = {'R': [0,1], 'L' : [0, -1], 'U' : [-1, 0], 'D' : [1, 0]}
    check = {(i, j) : [] for i in range(11) for j in range(11)}
    now = (5,5) # 현재 좌표
    for dir in dirs:
        next = (now[0] + dist[dir][0], now[1] + dist[dir][1]) # 다음 좌표
        if not(0<=next[0]<11) or not(0<=next[1]<11): # board를 넘어갈 시에는 가만히 있는다.
            continue
        if next not in check[now]: # 가지 않은 길이라면 갱신
            answer += 1
            check[now].append(next)
            check[next].append(now)
        now = next # 다음 좌표를 현재 좌표로
    return answer
