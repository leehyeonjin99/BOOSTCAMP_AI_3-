def solution(msg):
    answer = []
    alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    count = 1
    dictionary = {}
    for alphabet in alphabets:
        dictionary[alphabet]=count
        count+=1
    walker=0
    while walker<len(msg):
        len_word=1
        while msg[walker:walker+len_word] in dictionary and walker+len_word<=len(msg):
            len_word+=1
        answer.append(dictionary[msg[walker:walker+len_word-1]])
        dictionary[msg[walker:walker+len_word]]=count
        count+=1
        walker = walker+len_word-1
    return answer
