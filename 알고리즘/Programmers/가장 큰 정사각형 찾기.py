# 모든 값이 0인 경우 고려 X
# 효율성 테스트 불통
# def solution(board):
#     answer = 1234
#     max_len = min(len(board), len(board[0]))
#     for i in range(max_len, 0, -1):
#         for dx in range(len(board) - i + 1):
#             for dy in range(len(board[0]) - i + 1):
#                 check = True
#                 for b in board[dx : dx + i]:
#                     if 0 in b[dy : dy + i]:
#                         check = False
#                 if check:
#                     return i**2

#     return answer

def solution(board):
    answer = 0
    dp = [[0 for _ in range(len(board[0]) + 1)] for _ in range(len(board) + 1)]
    for i in range(1, len(board) + 1):
        for j in range(1, len(board[0])+ 1):
            if board[i-1][j-1] == 1:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])+1
            if dp[i][j] > answer:
                answer = dp[i][j]
    return answer ** 2
