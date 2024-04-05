import sys
from collections import *
from itertools import *
input = sys.stdin.readline

def bfs(com):
    start = com[0]
    q = deque([start])
    visited = set([start])
    now_sum = 0
    while q:
        now = q.popleft()
        now_sum += sp[now]
        for i in graph[now]:
            if i not in visited and i in com:
                q.append(i)
                visited.add(i)
    return now_sum, len(visited)

n = int(input())
sp = [int(x) for x in input().split()]
graph = defaultdict(list)
result = float('inf')


arr = [list(map(int,input().split()))[1:] for _ in range(n)]
for i in range(n):
    for j in arr[i]:
        graph[i].append(j-1)

for i in range(1, n//2 + 1):
    combis = list(combinations(range(n), i))
    for com in combis:
        sum1, len1 = bfs(com)
        sum2, len2 = bfs([i for i in range(n) if i not in com])
        if len1 + len2 == n:
            result = min(result, abs(sum1 - sum2))

print(result) if result != float('inf') else print(-1)