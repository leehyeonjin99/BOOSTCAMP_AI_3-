def solution(number, k):
    i = 0
    while i < len(number) -1 and k > 0 :
        if number[i] < number[i + 1]:
            number = number[:i] + number[i+1:]
            k -= 1
            # 만약 i = 0이었다면 계속 뒤에와 확인해라
            # 하지만, i > 0 이라면 앞에서부터 다시 확인해라
            if i > 0:
                i -= 1
        else:
            i += 1
    # 아직 제거해야할 개수가 남아있다면 뒤에서 제거
    if k > 0:
        number = number[:-k]
    return number
