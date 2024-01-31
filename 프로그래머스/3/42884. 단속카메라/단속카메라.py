from collections import deque

def solution(routes):
    routes.sort(key=lambda x: x[1])
    r = deque(routes)
    now = -30001
    result = 0
    while r:
        start,end = r.popleft()
        if start > now:
            now = end
            result += 1
    return result