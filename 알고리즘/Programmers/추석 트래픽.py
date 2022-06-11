def solution(lines):
    answer = 0
    starts = []
    ends = []
    for line in lines:
        date, time, T = line.split()
        time = (list(map(float, time.split(":"))))
        time = round(time[0] * 3600 + time[1] * 60 + time[2], 4)
        T = round(float(T[:-1]), 4)
        starts.append(round(time - T + 0.001, 4))
        ends.append(time)
    # print(starts)
    # print(ends)
    for end in ends:
        end_time = round(end + 0.999, 3)
        # print("="*5, end, end_time)
        count = 0
        for s, e in zip(starts, ends):
            # print(s, e, end = ": ")
            if (end <= s <= end_time or end <= e <= end_time) or (s <= end and end_time <= e):
                count += 1
                if answer < count:
                    answer = count
            #     print(True, count)
            # else:
            #     print(False)
    if answer <count:
        answer = count
        
    return answer
