import math
def solution(w,h):
    answer=0
    w, h = min(w, h), max(w, h) # for문을 더 적게 돌리기 위해서 : testcase 11
    if w == h : # 같은 경우는 간단하게 계산 가능하므로, for문을 제외 : testcase 12,14
        return w * h - w
    for idx in range(w):
        answer += math.ceil(-idx*h/w+h)-math.floor(-(idx+1)*h/w+h) # * 후 /를 한다. 소수의 epsilon이 붙는 경우 고려 : testcase 6
    return w * h - answer