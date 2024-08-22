from heapq import *

def solution(begin, target, words):
    h = [[0,begin]]
    heapify(h)
    visited = []
    
    while h:
        c, now = heappop(h)
        for i in range(len(begin)):
            for word in words:
                if now[:i] + now[i+1:] == word[:i] + word[i+1:] and word not in visited:
                    if word == target:
                        return c+1
                    visited.append(word)
                    heappush(h, [c+1, word])
    return 0