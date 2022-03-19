'''
# solution 1) 0.15ms
from itertools import permutations

def calculation(operation, seq, expression):
    if expression.isdigit():
        return str(expression)
    if operation[seq] == '*':
        split_data = expression.split('*')
        temp = []
        for data in split_data:
            temp.append(calculation(operation, seq + 1, data))
        return str(eval('*'.join(temp)))
    if operation[seq] == '+':
        split_data = expression.split('+')
        temp = []
        for data in split_data:
            temp.append(calculation(operation, seq + 1, data))
        return str(eval('+'.join(temp)))
    if operation[seq] == '-':
        split_data = expression.split('-')
        temp = []
        for data in split_data:
            temp.append(calculation(operation, seq + 1, data))
        return str(eval('-'.join(temp)))
            

def solution(expression):
    answer = 0
    for operation in permutations(["*", "+", "-"], 3):
        result = abs(int(calculation(operation, 0, expression)))
        if result > answer:
            answer = result
    return answer
 '''

# solution 2) 0.10ms
def solution(expression):
    answer = []
    operations = [['*', '+', '-'], ['*', '-', '+'], ['+', '*', '-'], ['+', '-', '*'], ['-', '*', '+'], ['-', '+', '*']]
    exp = ''
    for operation in operations:
        a = operation[0]
        b = operation[1]
        temp_list = []
        for first_split in expression.split(a):
            temp = [f"({second_split})" for second_split in first_split.split(b)]
            temp_list.append(f"({b.join(temp)})")
        answer.append(abs(eval(a.join(temp_list))))
        
    return max(answer)