def solution(files):
    answer = []
    for file in files:
        count=0
        idx=0
        head=''
        for f in file:
            if not f.isdigit():
                head+=f
                idx+=1
            else:
                break
        number=''
        for f in file[idx:]:
            if f.isdigit():
                number+=f
                idx+=1
            else:
                break
        tail=file[idx:]
        answer.append([head, number, tail])
    answer.sort(key=lambda x : (x[0].lower(),int(x[1])))
    for i in range(len(answer)):
        answer[i]=''.join(answer[i])
            
    return answer