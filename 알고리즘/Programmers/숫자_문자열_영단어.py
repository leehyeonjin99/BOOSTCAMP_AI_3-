def solution(s):
    answer = 0
    num={'zero':'0', 'one':'1','two':'2','three':'3',
        'four':'4','five':'5','six':'6','seven':'7',
        'eight':'8','nine':'9'}
    for i in range(10):
        word=list(num.keys())[i]
        s=s.replace(word,num[word])
    answer=int(s)
    return answer