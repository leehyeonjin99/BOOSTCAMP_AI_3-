import sys
from collections import deque
T=int(sys.stdin.readline())

next=[[-1,2],[-1,-2],[1,-2],[1,2],[2,1],[2,-1],[-2,1],[-2,-1]]

for _ in range(T):
    length=int(sys.stdin.readline())
    start=list(map(int, sys.stdin.readline().split()))
    end=list(map(int, sys.stdin.readline().split()))

    count=[[0 for _ in range(length)] for _ in range(length)]

    que=deque()
    que.append(start)
    count[start[0]][start[1]]=0

    while que:
        now_x, now_y=que.popleft()
        if now_x==end[0] and now_y==end[1]:
            print(count[now_x][now_y])
            break
        for next_dist in next:
            next_x=now_x+next_dist[0]
            next_y=now_y+next_dist[1]

            if 0<=next_x<length and 0<=next_y<length:
                if count[next_x][next_y]==0:
                    count[next_x][next_y]=count[now_x][now_y]+1
                    que.append([next_x,next_y])



