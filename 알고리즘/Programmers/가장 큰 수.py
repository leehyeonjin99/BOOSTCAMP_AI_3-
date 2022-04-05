def solution(numbers):
    numbers = list(map(str, numbers)) # 사전식으로 앞자리 부터 확인하기 위해서 str로 변경한다.
    numbers.sort(key = lambda x : x*3, reverse = True) # 1000이하의 인자를 갖기 때문에 3자리에 맞춰 비교하기 위해서 x*3을 한다.
    return str(int(''.join(numbers))) # 0000은 0으로 표현하기 위해 int로 type 설정 후 문제에서 원하는 answer는 str이므로 type을 재설정 한다.
