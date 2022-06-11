def padding(key, lock):
    padding_size = len(key) - 1
    origin_size = len(lock)
    padding = []
    count = 0
    for i in range(padding_size):
        padding.append([-1 for _ in range(2*padding_size + origin_size)])
    for lock_row in lock:
        for l in lock_row:
            if l == 0:
                count +=1
        padding.append([-1 for _ in range(padding_size)] + lock_row + [-1 for _ in range(padding_size)])
    for i in range(padding_size):
        padding.append([-1 for _ in range(2*padding_size + origin_size)])
    return padding, count

def sub_lock(lock, start_row, start_col, sub_size, key_num):
    tmp = []
    count = 0
    for row in range(start_row, start_row + sub_size):
        for col in range(start_col, start_col + sub_size):
            if lock[row][col] == 0:
                count += 1
        tmp.append(lock[row][start_col:start_col + sub_size])
    return tmp, count
    
def rotate(lock):
    return list(zip(*lock[::-1]))

def check(sub_lock, key):
    for row in range(len(key)):
        for col in range(len(key)):
            if sub_lock[row][col] == -1:
                continue
            elif sub_lock[row][col] != key[row][col]:
                # print(row, col)
                return False
    return True
    

def solution(key, lock): 
    lock, key_num = padding(key, lock)
    check_size = len(lock) - len(key) + 1
    # print(lock)
    
    for rot in range(4):
        for rot_num in range(rot):
            key = rotate(key)
        # print("="*5, key, key_num, "="*5)
        for row in range(check_size):
            for col in range(check_size):
                # print(row, col)
                sub, key_check = sub_lock(lock, row, col, len(key), key_num)
                sub = [[1 if v == 0 else (-1 if v == -1 else 0) for v in row] for row in sub]
                # print(sub, key_check, end = ": ")
                if key_check == key_num and check(sub, key):
                    print(True)
                    return True
                # else:
                #     print(False)
    return False
