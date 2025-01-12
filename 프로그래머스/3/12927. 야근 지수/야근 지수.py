from heapq import *

def solution(n, works):
    h = []
    for work in works:
        heappush(h, -work)

    while n > 0:
        if not h: 
            break
        max_val = -heappop(h) 
        if max_val > 0:
            max_val -= 1 
        heappush(h, -max_val) 
        n -= 1  

    return sum(x**2 for x in h)