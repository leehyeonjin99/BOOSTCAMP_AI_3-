def split_two(string):
    string = string.upper()
    multi_set = {}
    for index in range(len(string)-1):
        two = string[index:index+2]
        if two.isalpha():
            if two not in multi_set:
                multi_set[two] = 1
            else:
                multi_set[two] += 1
    return multi_set

import math

def J(dic1, dic2):
    elements = set(dic1.keys()) | set(dic2.keys())
    union = 0
    intersection = 0
    for element in elements:
        if element in dic1 and element in dic2:
            union += max(dic1[element], dic2[element])
            intersection += min(dic1[element], dic2[element])
        elif element in dic1:
            union += dic1[element]
        else:
            union += dic2[element]
    return math.floor(intersection / union * 65536) if union!=0 else 65536

def solution(str1, str2):
    str1 = split_two(str1)
    str2 = split_two(str2)    
    return J(str1, str2)