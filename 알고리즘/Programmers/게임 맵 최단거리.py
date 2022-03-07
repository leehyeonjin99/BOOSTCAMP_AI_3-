from collections import deque

def solution(maps):
    height, width = len(maps), len(maps[0])
    dx, dy = [0,0,1,-1], [1,-1,0,0]
    root = [[-1 for _ in range(width)] for _ in range(height)]
    que=deque([[0,0]])
    root[0][0]=1
    while que:
        x, y = que.popleft()
        for x_diff, y_diff in zip(dx, dy):
            next_x, next_y = x+x_diff, y+y_diff
            if 0<=next_x<width and 0<=next_y<height and root[next_y][next_x]==-1 and maps[next_y][next_x]==1:
                root[next_y][next_x]=root[y][x]+1
                que.append([next_x, next_y])
    answer=root[-1][-1]    
    return answer
