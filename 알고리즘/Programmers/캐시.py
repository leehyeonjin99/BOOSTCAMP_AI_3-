from collections import deque
def solution(cacheSize, cities):
    time = 0
    cache = deque(maxlen = cacheSize)
    for city in cities:
        city = city.lower()
        check = True if city in cache else False
        if check:
            time += 1
            cache.remove(city)
        else:
            time += 5    
        cache.append(city)
    return time
