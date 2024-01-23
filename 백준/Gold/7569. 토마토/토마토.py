import sys
from collections import deque
input = sys.stdin.readline

m, n, h = list(map(int,input().split(' ')))
in_m = range(m)
in_n = range(n)
in_h = range(h)

box = {}
for floor in range(h):
    box[floor] = []
    for _ in range(n):
        box[floor].append(list(map(int,input().split(' '))))
                          
real_tomato = deque()

for floor in box:
    for arr in range(len(box[floor])):
        for tomato in range(len(box[floor][arr])):
            if box[floor][arr][tomato] == 1:
                real_tomato.append([floor, arr, tomato])

next_day = []
result = 0
while real_tomato:
    now_h, now_s, now_g = real_tomato.popleft()
    for adj_h, adj_s, adj_g in [[1, 0, 0],[-1,0,0],[0,1,0],[0,-1,0],[0,0,1],[0,0,-1]]:
        next_h, next_s, next_g = now_h + adj_h, now_s + adj_s, now_g + adj_g
        if next_h in in_h and next_s in in_n and next_g in in_m and box[next_h][next_s][next_g] == 0:
            box[next_h][next_s][next_g] = 1
            next_day.append([next_h, next_s, next_g])
    if not real_tomato:
        result += 1
        real_tomato.extend(next_day)
        next_day = []

for floor in box:
    for arr in range(len(box[floor])):
        for tomato in range(len(box[floor][arr])):
            if box[floor][arr][tomato] == 0:
                print(-1)
                exit()

print(result-1)