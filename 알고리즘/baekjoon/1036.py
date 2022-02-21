import sys

N=int(sys.stdin.readline())
char_cnt=[[] for _ in range(36)]
S=0
for _ in range(N):
    word=sys.stdin.readline()
    seat=len(word)-2
    S+=int(word,36)
    for c in word:
        if c=='\n':
            continue
        char_cnt[int(c,36)].append(seat)
        seat-=1
K=int(sys.stdin.readline())
temp=[]
for num,seats in enumerate(char_cnt):
    diff=0
    if seats:
        for seat in seats:
            diff+=(int('Z',36)-num)*(36**seat)
    temp.append(diff)

temp.sort(reverse=True)
S+=sum(temp[:K])

def to_36(N):
    d=list('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    a, b=N//36, N%36
    w=d[b]
    return to_36(a)+w if a!=0 else w

print(to_36(S))