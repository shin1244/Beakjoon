from collections import deque

def solution(numbers, target):
    q = deque()
    q.append(0)
    temp = deque()

    for number in numbers:
        while q:
            now = q.popleft()
            temp.append(now+number)
            temp.append(now-number)
        q, temp = temp, deque()
    
    return q.count(target)