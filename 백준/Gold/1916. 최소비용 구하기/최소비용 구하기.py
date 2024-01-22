from heapq import *
import sys

input = sys.stdin.readline

city = int(input())
bus = int(input())
arr = [list(map(int, input().split(' '))) for _ in range(bus)]
s, e = list(map(int, input().split(' ')))

cost_dict = {i: 1e9 for i in range(1, city+1)}

bus_dict = {}
for i, j, k in arr:
    if i in bus_dict:
        bus_dict[i].append([j, k])
    else:
        bus_dict[i] = [[j, k]]
cost_dict[s] = 0


for key in range(1, city+1):
    if key not in bus_dict:
        bus_dict[key] = []

h = []
heappush(h, [cost_dict[s], s])

while h:
    now_sum, now_num = heappop(h)

    if cost_dict[now_num] < now_sum:
        continue

    for i, j in bus_dict[now_num]:
        sum_cost = now_sum + j
        if sum_cost < cost_dict[i]:
            cost_dict[i] = sum_cost
            heappush(h, [sum_cost, i])

print(cost_dict[e])