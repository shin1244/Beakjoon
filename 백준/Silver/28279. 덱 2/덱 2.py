from collections import deque
import sys

input=sys.stdin.readline
n = int(input())
arr = [list(map(int, input().split(' '))) for _ in range(n)]

q = deque()

for i in arr:
    if i[0] == 1:
        q.appendleft(i[1])
    elif i[0] == 2:
        q.append(i[1])
    elif i[0] == 3:
        print(q.popleft()) if q else print(-1)
    elif i[0] == 4:
        print(q.pop()) if q else print(-1)
    elif i[0] == 5:
        print(len(q))
    elif i[0] == 6:
        print(0) if len(q) else print(1)
    elif i[0] == 7:
        print(q[0]) if q else print(-1)
    elif i[0] == 8:
        print(q[-1]) if q else print(-1)