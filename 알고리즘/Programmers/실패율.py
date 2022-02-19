def solution(N, stages):
    challenger = [0 for _ in range(N+1)]
    for stage in stages:
        for i in range(stage):
            challenger[i]+=1
    success=[]
    for i in range(N):
        success.append(challenger[i]-challenger[i+1])
    temp=[]
    for i in range(N):
        temp.append([i+1,success[i]/challenger[i]] if challenger[i]!=0 else [i+1,0])
    temp.sort(key=lambda x : (-x[1],x[0]))
    print(temp)
    answer=[]
    for key, value in temp:
        answer.append(key)
        
    return answer