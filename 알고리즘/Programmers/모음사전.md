def solution(word):
    answer = 0
    num_of_char = 5
    word_order = {'A':0, 'E':1, 'I':2, 'O':3, 'U':4}
    total = 0
    for i in range(num_of_char):
        total += num_of_char**(i+1)
    for idx, w in enumerate(word):
        answer += (total // num_of_char**(idx+1)) * word_order[w] + 1
    return answer
