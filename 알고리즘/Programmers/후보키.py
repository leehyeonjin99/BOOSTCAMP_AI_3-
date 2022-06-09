from itertools import combinations

def solution(relation):
    answer = 0
    not_key = range(len(relation[0]))
    key = []
    number = 1
    while number <= len(relation[0]):
        for comb in combinations(not_key, number):
            count_dict = {}
            for people in relation:
                people_list = ""
                for c in comb:
                    people_list += str(people[c])
                if people_list not in count_dict:
                    count_dict[people_list] = 1
                else:
                    count_dict[people_list] += 1
            if all(x<2 for x in count_dict.values()):
                new_key = ''.join(list(map(str, comb)))
                if all(any(old not in new_key for old in old_key) for old_key in key):
                    key.append(new_key)
                    answer += 1
        number += 1
                    
    return answer
