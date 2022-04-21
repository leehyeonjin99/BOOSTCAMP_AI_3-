def explore(k, dungeons, num, answers):
    if len(dungeons) == 1:
        if k >= max(dungeons[0]):
            k -= dungeons[0][1]
            answers.append(num + 1)
            return
        else:
            answers.append(num)
            return
    for idx, dungeon in enumerate(dungeons):
        if k >= max(dungeon):
            explore(k-dungeon[1], dungeons[:idx] + dungeons[idx+1:], num+1, answers)
        else:
            explore(k, dungeons[:idx] + dungeons[idx+1:], num, answers)
            

def solution(k, dungeons):
    answers = []
    explore(k, dungeons, 0, answers)
    return max(answers)
