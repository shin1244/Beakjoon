from collections import deque

def solution(people, limit):
    people.sort()
    people = deque(people)
    result = 0
    while people:
        result += 1
        now_wieght = people.pop()
        if people and limit - (now_wieght + people[0]) >= 0:
            people.popleft()
        
    return result