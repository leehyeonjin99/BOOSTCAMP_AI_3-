import math
def solution(numbers, hand):
    answer = ''
    location={1:[0,0], 2:[0,1], 3:[0,2],
              4:[1,0], 5:[1,1], 6:[1,2],
              7:[2,0], 8:[2,1], 9:[2,2],
              0:[3,1]}
    left_location=[3,0]
    right_location=[3,2]
    left=[1,4,7]
    right=[3,6,9]
    for number in numbers:
        if number in left:
            answer+='L'
            left_location=location[number]
        elif number in right:
            answer+='R'
            right_location=location[number]
        else:
            number_location=location[number]
            left_dist=abs(number_location[0]-left_location[0])+abs(number_location[1]-left_location[1])
            right_dist=abs(number_location[0]-right_location[0])+abs(number_location[1]-right_location[1])
            if left_dist<right_dist or (left_dist==right_dist and hand=='left'):
                answer+='L'
                left_location=number_location
            elif left_dist>right_dist or (left_dist==right_dist and hand=='right'):
                answer+='R'
                right_location=number_location
            
    return answer