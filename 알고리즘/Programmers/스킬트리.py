def solution(skill, skill_trees):
    answer = 0
    for skill_tree in skill_trees:
        tmp = []
        check = False
        for s in skill:
            try:
                tmp.append(skill_tree.index(s))
            except:
                tmp.append(30)
        if sorted(tmp) == tmp:
            print(skill_tree)
            answer += 1
    return answer
