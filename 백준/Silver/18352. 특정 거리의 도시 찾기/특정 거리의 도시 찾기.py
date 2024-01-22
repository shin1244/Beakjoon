import sys
from heapq import *
input = sys.stdin.readline 
nodes, n, target, start = list(map(int,input().split(' ')))
arr = [list(map(int,input().split(' '))) for _ in range(n)]

graph_dict = {}
for i,j in arr:
    if i in graph_dict:
        graph_dict[i].append(j)
    else:
        graph_dict[i] = [j]

for key in range(1, nodes+1):
    if key not in graph_dict:
        graph_dict[key] = []

cost_dict = {i:1e9 for i in range(1, nodes+1)}
h = [[0, start]]
visited = set()

while h and h[0][0] < target:
    now_cost, now_num = heappop(h)
    visited.add(now_num)
    for i in graph_dict[now_num]:
        if i not in visited:
            now_sum = now_cost + 1
            if cost_dict[i] > now_sum:
                cost_dict[i] = now_sum
                heappush(h, [now_sum, i])
if not h:
    print(-1)
else:
    answer = sorted([i[1] for i in h])
    for i in answer:
        print(i)