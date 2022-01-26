def solution(dartResult):
    dartResult=calcul(dartResult)
    answer= []
    count=0
    for i in range(len(dartResult)):
        if dartResult[i].isdigit():
            subanswer=int(dartResult[i])
        else:
            if dartResult[i]=='S':
                subanswer=subanswer
            elif dartResult[i]=='D':
                subanswer=subanswer**2
            elif dartResult[i]=='T':
                subanswer=subanswer**3
            elif dartResult[i]=='*':
                subanswer=subanswer*2
                if count!=0:
                    answer[count-1]=answer[count-1]*2
            elif dartResult[i]=='#':
                subanswer=-subanswer
        if i!=len(dartResult)-1 and dartResult[i+1].isdigit():
            answer.append(subanswer)
            count+=1
        elif i==len(dartResult)-1:
            answer.append(subanswer)
            count+=1
    print(answer)
    answer=sum(answer)
    return answer

def calcul(s):
    result=[]
    i=0
    while i<len(s):
        if i!=len(s)-1 and s[i]=='1' and s[i+1]=='0':
            result.append(s[i]+s[i+1])
            i+=2
        else:
            result.append(s[i])
            i+=1
    return result