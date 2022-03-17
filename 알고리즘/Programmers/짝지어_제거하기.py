def solution(s):
    stack = []
    for i in s:
        stack.pop() if stack and stack[-1] == i else stack.append(i)
    return 1 if not stack else 0

# 질문
# stack.pop()을 사용할 때와 stack[:-1]을 사용할 때의 시간 복잡도의 차이는?
# pop : O(1)
# list slicing : O(원소 개수)