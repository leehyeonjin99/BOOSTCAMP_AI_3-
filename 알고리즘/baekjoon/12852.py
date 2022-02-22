import sys

N=int(sys.stdin.readline())
cnt_list=[[0,[]] for _ in range(N+1)]
cnt_list[1][0]=0
cnt_list[1][1]=[1]

for i in range(2, N+1):

    cnt_list[i][0]=cnt_list[i-1][0]+1
    cnt_list[i][1]=[i]+cnt_list[i-1][1]

    if i%3==0 and cnt_list[i][0]>cnt_list[i//3][0]+1:
        cnt_list[i][0]=cnt_list[i//3][0]+1
        cnt_list[i][1]=[i]+cnt_list[i//3][1]
    if i%2==0 and cnt_list[i][0]>cnt_list[i//2][0]+1:
        cnt_list[i][0]=cnt_list[i//2][0]+1
        cnt_list[i][1]=[i]+cnt_list[i//2][1]

print(cnt_list[N][0])
print(*cnt_list[N][1])

    
    