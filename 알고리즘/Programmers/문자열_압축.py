def solution(s):
    answer = len(s)
    for i in range(1,len(s)//2+1):
        idx=0
        words=[]
        while idx<len(s):
            if idx+i<len(s):
                words.append(s[idx:idx+i])
            else:
                words.append(s[idx:])
            idx+=i
        result=''
        count=1
        for i in range(len(words)):
            if i<len(words)-1:
                if words[i]==words[i+1]:
                    count+=1
                    if i+1==len(words)-1:
                        result+=str(count)+words[i]
                else:
                    if count==1:
                        result+=words[i]
                    else:
                        result+=str(count)+words[i]
                    count=1
            else:
                if words[i-1]!=words[i]:
                    result+=words[i]
        if len(result)<answer:
            answer=len(result)
    return answer