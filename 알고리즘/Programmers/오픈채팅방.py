def solution(record):
    answer=[]
    dict={}
    for rec in record:
        rec=rec.split()
        if rec[0]=='Enter':
            answer.append([rec[1],'님이 들어왔습니다.'])
            dict[rec[1]]=rec[2]
        elif rec[0]=='Leave':
            answer.append([rec[1],'님이 나갔습니다.'])
        elif rec[0]=='Change':
            dict[rec[1]]=rec[2]
    
    for ind, ans in enumerate(answer):
        answer[ind]=dict[ans[0]]+ans[1]
    return answer

'''
# 81/100 (시간초과)
def solution(record):
    answer = []
    name_dict={}
    for index,rec in enumerate(record):
        rec=rec.split()
        if rec[0]=='Enter':
            if rec[1] not in name_dict.keys():
                name_dict[rec[1]]=[[index,rec[0],rec[2]]]
            else:
                name_dict[rec[1]].append([index, rec[0],rec[2]])
                for i in range(len(name_dict[rec[1]])):
                    name_dict[rec[1]][i][2]=rec[2]
        elif rec[0]=='Change':
            for i in range(len(name_dict[rec[1]])):
                name_dict[rec[1]][i][2]=rec[2]
        elif rec[0]=='Leave':
            name_dict[rec[1]].append([index,rec[0],name_dict[rec[1]][-1][2]])
    
    result=sum(list(name_dict.values()),[])
    result.sort()
    for res in result:
        if res[1]=='Enter':
            answer.append(f"{res[2]}님이 들어왔습니다.")
        elif res[1]=='Leave':
            answer.append(f"{res[2]}님이 나갔습니다.")
    return answer
'''