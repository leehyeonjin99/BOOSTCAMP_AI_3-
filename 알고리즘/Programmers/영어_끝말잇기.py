import math
def solution(n, words):
    answer = [0,0]
    game = []
    for word in words:
        if word not in game and not (game and game[-1][-1]!=word[0]):
            game.append(word)   
        else:
            return [(len(game)+1) % n if (len(game)+1) % n else n, math.ceil((len(game)+1) / n)]
    return answer
