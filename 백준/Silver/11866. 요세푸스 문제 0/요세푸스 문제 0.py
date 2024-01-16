n = list(map(int,input().split()))

from collections import deque

people = deque()
for i in range(1, n[0]+1): people.append(i)
result = []

while people:
    for _ in range(n[1]-1):
        people.append(people.popleft())
    result.append(people.popleft())

print(str(result).replace('[', '<').replace(']', '>'))