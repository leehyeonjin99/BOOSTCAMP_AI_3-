from itertools import combinations
from collections import defaultdict
from bisect import bisect_left

def solution(information, queries):
    answer = []
    dic = defaultdict(list)
    for info in information:
        info = info.split()
        condition = info[:-1]  
        score = int(info[-1])
        for i in range(5):
            case = list(combinations(range(4), i))
            for c in case:
                tmp = condition.copy()
                for idx in c:
                    tmp[idx] = "-"
                key = ''.join(tmp)
                dic[key].append(score) 

    for value in dic.values():
        value.sort()   

    for query in queries:
        query = query.replace("and ", "")
        query = query.split()
        target_key = ''.join(query[:-1])
        target_score = int(query[-1])
        count = 0
        if target_key in dic:
            target_list = dic[target_key]
            idx = bisect_left(target_list, target_score)
            count = len(target_list) - idx
        answer.append(count)      
    return answer

'''
정확성만 통과한 테스트
def solution(info, query):
    info=[i.split() for i in info]
    answer=[]
    for q in query:
        q=q.split(" and ")[:-1]+q.split(" and ")[-1].split()
        print(q)
        count=0
        for i in info:
            if q[0]!='-' and i[0]!=q[0]:
                continue
            if q[1]!='-' and i[1]!=q[1]:
                continue
            if q[2]!='-' and i[2]!=q[2]:
                continue
            if q[3]!='-' and i[3]!=q[3]:
                continue
            if int(i[4])<int(q[4]):
                continue
            count+=1
        answer.append(count)
    return answer
'''