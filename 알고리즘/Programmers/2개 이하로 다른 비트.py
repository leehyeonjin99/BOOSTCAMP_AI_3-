def sub_sol(number):
    # 짝수인 경우 : ex. 1100 → 1111
    if number %2 == 0:
        return number + 1
    # 홀수인 경우 : ex. 1111 → 10111, 1101 → 1110
    # 가장 처음 나오는 0을 1로 변결우 앞의 수를 0으로 바꾼다.
    else:
        tmp = str(bin(number)[2:])
        tmp = tmp[::-1]
        if "0" in tmp:
            change_0 = tmp.index("0")
            change_1 = change_0 - 1
            tmp = tmp[:change_0] + "1" + tmp[change_0+1:]
            if change_1 >= 0:
                tmp = tmp[:change_1] + "0" + tmp[change_1+1:]
            return int(tmp[::-1],2)
        else:
            tmp = "10"+tmp[::-1][1:]
            return int(tmp, 2)
        
def solution(numbers):
    answer = []
    for num in numbers:
        num = int(num)
        answer.append(sub_sol(num))
    return answer
