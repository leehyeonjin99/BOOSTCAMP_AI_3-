def solution(n, t, m, timetable):
    answer=''
    seat={9*60+t*i:[] for i in range(n)}
    for idx,time in enumerate(timetable):
        hour_min=list(map(int, time.split(':')))
        timetable[idx]=hour_min[0]*60+hour_min[1]
    timetable.sort()
    for time in timetable:        
        for s in seat.keys():
            if time<=s and len(seat[s])<m:
                seat[s].append(time)
                break
                
    print(seat)
    if len(seat[9*60+(n-1)*t])<m:
        answer=9*60+(n-1)*t
        answer=str(answer//60).zfill(2)+':'+str(answer%60).zfill(2)
    else:
        answer=seat[9*60+(n-1)*t][-1]-1
        print(answer)
        answer=str(answer//60).zfill(2)+':'+str(answer%60).zfill(2)
    return answer