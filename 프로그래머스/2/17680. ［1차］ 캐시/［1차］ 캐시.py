from collections import deque

def solution(cacheSize, cities):
    cache = deque()
    cities = deque(cities)
    result = 0

    while cities:
        city = cities.popleft()
        city = city.upper()
        if city in cache:
            result += 1
            cache.remove(city)
            cache.append(city)
        else:
            result += 5
            cache.append(city)
            if len(cache) > cacheSize:
                cache.popleft()
    
    return result

2, ["Jeju", "Pangyo", "NewYork", "newyork"]