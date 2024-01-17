import sys
from heapq import heappush, heappop

n = int(sys.stdin.readline().strip())
min_heap = []
max_heap = []
result = []

for i in range(n):
    now = int(sys.stdin.readline().strip())
    if len(min_heap) == len(max_heap):
        heappush(max_heap, -now)
    else:
        heappush(min_heap, now)
    if max_heap and min_heap and -max_heap[0] > min_heap[0]:
        min_0 = -heappop(min_heap)
        max_0 = -heappop(max_heap)
        heappush(max_heap, min_0)
        heappush(min_heap, max_0)

    result.append(-max_heap[0])

for j in result:
    print(j)
