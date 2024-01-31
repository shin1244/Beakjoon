from collections import deque

def solution(n, k):
    a = len(n) - k
    now, b = n[:-a], deque(n[-a:])
    result = ''
    
    while b:
        now+=b.popleft()
        if '9' in now:
            now_max = '9'
        else:
            now_max = max(now)
        result += now_max
        max_index = now.index(now_max)
        now = now[max_index+1:]
        
    return result