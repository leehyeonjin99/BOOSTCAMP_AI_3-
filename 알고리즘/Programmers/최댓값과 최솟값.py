def solution(s):
    answer = ''
    nums = list(map(int, s.split()))
    answer = ' '.join(map(str, [min(nums), max(nums)]))
    return answer
