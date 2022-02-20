def solution(s):
    answer = []
    L=[]
    s=s[2:-2].split('},{')
    for nums in s:
        L.append(list(map(int, nums.split(','))))
    L.sort(key=lambda x : len(x))
    answer.append(L[0][0])
    for idx in range(1, len(L)):
        diff=set(L[idx])-set(L[idx-1])
        answer.append(list(diff)[0])
    return answer