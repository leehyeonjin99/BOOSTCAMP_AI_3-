from itertools import combinations

def solution(clothes):
    answer = 1
    kind_num = 0
    closet = {}
    for cloth, kind in clothes:
        if kind in closet:
            closet[kind][0] += 1
            closet[kind][1].append(cloth)
        else:
            kind_num += 1
            closet[kind] = [1, [cloth]]
####################### 시간 초과 ######################
#     for n in range(1, kind_num+1):
#         for combs in combinations(closet.keys(), n):
#             mult = 1
#             for comb in combs:
#                 mult *= closet[comb][0]
#             answer += mult
#     return answer
#######################################################
    for kind, num_clothes in closet.items():
        print(num_clothes)
        answer *= num_clothes[0]+1 # 옷 종류 + 1(안입은 경우)
    return answer -1 # 모든 옷을 안입은 경우를 뺴준다
