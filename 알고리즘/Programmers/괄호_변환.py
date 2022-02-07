def solution(p):
    if not p:
        return p
    left=0
    right=0
    u=''
    v=''
    check=True
    for alph in p:
        if alph=='(':
            left+=1
        elif alph==')':
            right+=1
        if check:
            u+=alph
        else:
            v+=alph
        if left==right:
            check=False
    if balance(u):
        return u+solution(v)
    else:
        result='('+solution(v)+')'
        u=u[1:-1]
        print(u)
        u=u.replace('(','0')
        u=u.replace(')','1')
        u=u.replace('0',')')
        u=u.replace('1','(')
        return result+u

def balance(p):
    que=[]
    for alph in p:
        if alph=='(':
            que.append(1)
        else:
            if que:
                que.pop()
            else:
                return False
    return True