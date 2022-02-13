def solution(places):
    answer=[int(dist_check(case)) for case in places]
    return answer

import math

def dist_check(case):
    check=True
    for i in range(5):
        for j in range(5):
            if case[i][j]=='P':
                if i+1<5 and case[i+1][j]=='P':
                    return False
                elif i+2<5 and case[i+1][j]!='X' and case[i+2][j]=='P':
                    return False
                elif j+1<5 and case[i][j+1]=='P':
                    return False
                elif j+2<5 and case[i][j+1]!='X' and case[i][j+2]=='P':
                    return False
                elif i+1<5 and j+1<5 and case[i+1][j+1]=='P' and (case[i+1][j]!='X' or case[i][j+1]!='X'):
                    return False
                elif i+1<5 and j-1>=0 and case[i+1][j-1]=='P' and (case[i+1][j]!='X' or case[i][j-1]!='X'):
                    return False
    return True

