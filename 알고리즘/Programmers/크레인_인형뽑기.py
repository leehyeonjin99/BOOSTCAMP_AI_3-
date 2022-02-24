from collections import deque

def solution(board, moves):
    answer = 0
    dolls=[deque([]) for _ in range(len(board)+1)]
    for i in range(len(board)):
        line=1
        for j in range(len(board)):
            if board[i][j]!=0:
                dolls[line].append(board[i][j])
            line+=1
    bascket=[]
    for move in moves:
        if dolls[move]:
            doll=dolls[move].popleft()
            if bascket and doll==bascket[-1]:
                answer+=2
                bascket=bascket[:-1]
            else:
                bascket.append(doll)
        
    return answer
