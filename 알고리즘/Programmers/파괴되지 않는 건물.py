def solution(board, skill):
    answer = 0
    row, col = len(board), len(board[0])
    tmp = [[0 for _ in range(col+1)] for _ in range(row+1)]
    for who, r1, c1, r2, c2, degree in skill:
        # 
        # for row in range(r1, r2 + 1):
        #     for col in range(c1, c2 + 1):
        #         if who == 1:
        #             board[row][col] -= degree
        #         else:
        #             board[row][col] += degree
        degree = degree if who == 2 else -degree
        tmp[r1][c1] += degree
        tmp[r2 + 1][c1] -= degree
        tmp[r1][c2 + 1] -= degree
        tmp[r2 + 1][c2 + 1] += degree
    # for b in tmp:
    #     print(*b)
    # print("="*10)
    for r in range(0, row):
        for c in range(1, col):
            tmp[r][c] += tmp[r][c-1]
    for r in range(1, row):
        for c in range(col):
            tmp[r][c] +=  tmp[r-1][c]
    # for b in tmp:
    #     print(*b)
    for r in range(row):
        for c in range(col):
            if board[r][c] + tmp[r][c] > 0:
                answer += 1
    
    return answer
