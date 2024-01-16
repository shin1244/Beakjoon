import sys
from heapq import heappush, heappop

n = int(sys.stdin.readline().strip())
arr = [int(sys.stdin.readline().strip()) for _ in range(n)]

h = []

for i in arr:
    if i != 0:
        heappush(h, -i)
    else:
        if h:
            print(-heappop(h))
        else:
            print(0)
