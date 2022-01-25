
T = int(input())

def solution(N,S):
    solution=[]
    for line in board:
        L=[i for i in line if i!=0]
        n=len(L)
        for i in range(n-1):
            if L[i]==L[i+1]:
                L[i]+=L[i+1]
                for j in range(i+1,n):
                    if j==n-1:
                        L[j]=0
                    else:
                        L[j]=L[j+1]
        solution.append(L+[0]*(N-n))
    return solution

def rotate(N,matrix):
    ret=[[0]*N for _ in range(N)]

    for r in range(N):
        for c in range(N):
            ret[c][N-1-r]=matrix[r][c]
    return ret

dic={"left":0,"down":1,"right":2,"up":3}

for test_case in range(1, T + 1):
    N,S=input().split()
    N=int(N)
    board=[]
    for _ in range(N):
        board.append(list(map(int,input().split())))
    for _ in range(dic[S]):
        board=rotate(N,board)
    board=solution(N,S)
    for _ in range((4-dic[S])%4):
        board=rotate(N,board)
    print("#{}".format(test_case))
    for i in range(N):
        print(*board[i])
    
