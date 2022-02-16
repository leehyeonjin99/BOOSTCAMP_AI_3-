import sys
from collections import deque
T=int(sys.stdin.readline())
for _ in range(T):
    N, dest= map(int, sys.stdin.readline().split())
    num=range(N)
    important=list(map(int, sys.stdin.readline().split()))
    num=deque(num)
    important=deque(important)
    count=0
    while num:
        M=max(important)
        now_doc, now_important=num.popleft(), important.popleft()
        if now_important<M:
            num.append(now_doc)
            important.append(now_important)
        else:
            count+=1
            if now_doc==dest:
                print(count)
                break

