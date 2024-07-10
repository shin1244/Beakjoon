from heapq import *

def solution(book_time):
    time_arr = []
    for s, e in book_time:
        start = s.split(":")
        end = e.split(":")
        
        start_time = int(start[0]) * 60 + int(start[1])
        end_time = int(end[0]) * 60 + int(end[1])
        
        time_arr.append([start_time, end_time])
    
    result = 1
    h = [0]
    heapify(h)
    for s, e in sorted(time_arr):
        if h[0] + 10 <= s:
            heappop(h)
            heappush(h, e)
        else:
            heappush(h, e)
            result += 1
            
    return result