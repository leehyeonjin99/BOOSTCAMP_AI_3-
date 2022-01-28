import math

def solution(fees, records):
    answer = []
    records_dict={}
    for record in records:
        record=record.split()
        HOUR, MIN=map(int,record[0].split(':'))
        TIME=HOUR*60+MIN
        CAR=int(record[1])
        IN_OUT=record[2]
        if CAR not in records_dict.keys():
            records_dict[CAR]=[]
        records_dict[CAR].append(TIME)

    for CAR, RECORDS in records_dict.items():
        TOTAL=0
        if len(RECORDS)%2!=0:
            TOTAL+=60*23+59
        for i,record in enumerate(RECORDS):
            if i%2==0:
                TOTAL-=record
            else:
                TOTAL+=record
        fee=fees[1]
        if TOTAL>fees[0]:
            fee+=math.ceil((TOTAL-fees[0])/fees[2])*fees[3]
            
        records_dict[CAR]=fee
    result=[[car,fee] for car,fee in records_dict.items()]
    result.sort(key=lambda x : x[0])
    answer=[x for car,x in result]
    return answer
