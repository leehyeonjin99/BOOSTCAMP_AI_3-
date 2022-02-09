from itertools import combinations

def solution(orders, course):
    answer=[]
    for order in orders:
        order=list(order)
        order.sort()
        answer.append(order)
    count=[{} for _ in range(len(course))]
    for ans in answer:
        for i,cour in enumerate(course):
            for comb in combinations(ans,cour):
                if comb in list(count[i].keys()):
                    count[i][comb]+=1
                else:
                    count[i][comb]=1
    print(count)
    answer=[]
    for cour in count:
        if cour:
            M=max(list(cour.values()))
            if M>=2:
                for key, value in cour.items():
                    if value==M:
                        answer.append(''.join(key))
    answer.sort()
            
    return answer