from collections import deque
def solution(begin, target, words):
    answer = 0
    if target not in words:
        return answer
    que = deque([])
    que.append([begin, words, 0])
    while que:
        now, words, count = que.popleft()
        # print("=================================")
        # print('"'+now+'" can be changed in', words)
        if now == target:
            # print("Finished")
            return count
        for word in words:
            diff_count = 0
            for n, w in zip(now, word):
                diff_count = diff_count + 1 if n!=w else diff_count
                if diff_count > 1:
                    break
            if diff_count == 1:
                # print(word)
                tmp_words = words.copy()
                tmp_words.remove(word)
                que.append([word, tmp_words, count + 1])
    return answer
