T=int(input())

for test_case in range(1, T + 1):
    a, b=map(int,input().split())
    if a>b:
        a,b=b,a
    level=0
    level_count=1
    count=0
    coordinate_dict={}
    for i in range(1,1+b):
        coordinate_dict[i]=[level, count]
        count+=1
        if count==level_count:
            level+=1
            level_count+=1
            count=0
    coord_a=coordinate_dict[a]
    coord_b=coordinate_dict[b]
    if coord_a[0]==coord_b[0]:
        dist=coord_b[1]-coord_a[1]
    else:
        if coord_a[1]>coord_b[1]:
            dist=coord_b[0]-coord_a[0]+coord_a[1]-coord_b[1]
        else:
            dist=coord_b[0]-coord_a[0]
            if dist<coord_b[1]-coord_a[1]:
                dist=coord_b[1]-coord_a[1]
    print(f"#{test_case} {dist}")