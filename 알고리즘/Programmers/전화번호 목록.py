# sort 사용 풀이 : 2.23ms
def solution(phone_book):
    phone_book.sort(key=lambda x : (x, len(x)))
    for i in range(len(phone_book)-1):
        i_len = len(phone_book[i])
        if phone_book[i] == phone_book[i+1][:i_len]:
            return False
    return True

# hash 사용 풀이 : 3.94
# def solution(phone_book):
#     answer = True
#     hash_map = {}
#     for phone_number in phone_book:
#         hash_map[phone_number] = 1
#     for phone_number in phone_book:
#         temp = ""
#         for number in phone_number:
#             temp += number
#             if temp in hash_map and temp != phone_number:
#                 answer = False
#     return answer
