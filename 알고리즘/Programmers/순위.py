def solution(n, results):
    answer = 0
    win = {i: set([]) for i in range(1, n+1)}
    loss = {i: set([]) for i in range(1, n+1)}
    for winner, losser in results:
        win[winner].add(losser)
        loss[losser].add(winner)
    # a는 b,c를 이겼다. / a는 d에게 졌다. -> d > a > b,c
    # d는 b,c를 이겼다. / b,c는 d에게 졌다.
    for i in range(1, n+1):
        for losser in win[i]:
            loss[losser] |= (loss[i])
        for winner in loss[i]:
            win[winner] |= (win[i])
    for win_, loss_ in zip(win.values(), loss.values()):
        if len(win_) + len(loss_) == n-1:
            answer += 1
    return answer
