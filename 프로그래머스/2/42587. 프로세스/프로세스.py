from collections import deque

def solution(priorities, location):
    priorities = deque(priorities)
    temp = deque(range(len(priorities)))
    result = 0
    
    while temp:
        now_number = priorities.popleft()
        now_index = temp.popleft()
        pri_check = 1
        
        for i in priorities:
            if now_number < i:
                priorities.append(now_number)
                temp.append(now_index)
                pri_check = 0
                break
        
        if pri_check:
            result += 1
            if now_index == location: return result