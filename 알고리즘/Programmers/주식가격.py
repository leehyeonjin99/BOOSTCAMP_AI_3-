# test3 180.42
# def solution(prices):
#     answer = []
#     for i in range(len(prices)):
#         start = prices[i]
#         answer.append(0)
#         for j in range(i+1, len(prices)):
#             answer[i] += 1
#             if start > prices[j]:
#                 break       
#     return answer

# test3 40.15
def solution(prices):
    stack = []
    answer = [0] * len(prices)
    for i in range(len(prices)):
        if stack != []:
            while stack != [] and stack[-1][1] > prices[i]:
                past, _ = stack.pop()
                answer[past] = i - past
        stack.append([i, prices[i]])
        print(stack)
    for i, s in stack:
        answer[i] = len(prices) - 1 - i
    return answer
