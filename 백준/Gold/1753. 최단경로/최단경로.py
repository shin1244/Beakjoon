from heapq import *
import sys
input = sys.stdin.readline

n, m = map(int,input().split(' '))

start = int(input())

graph = [[] for _ in range(n+1)]
for i in range(m):
    node1, node2, weight = map(int, input().split(' '))
    graph[node1].append([weight,node2])

DP = [float('inf')] * (n+1)

h = []
heappush(h, (0,start))
DP[start] = 0

while h:
    w, idx = heappop(h)
    if DP[idx] < w:
        continue
    for i in graph[idx]:
        now_w = w+i[0]
        if now_w < DP[i[1]]:
            DP[i[1]] = now_w
            heappush(h, (now_w, i[1]))

for i in DP[1:]:
    if i == float('inf'):
        print("INF")
    else:
        print(i)