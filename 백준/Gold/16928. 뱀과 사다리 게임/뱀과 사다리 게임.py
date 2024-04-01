from collections import *
import sys
input = sys.stdin.readline

ladders, snakes = map(int,input().split(' '))

DP = set()

ladder = {}
for _ in range(ladders):
    i, j = map(int, input().split())
    ladder[i] = j

snake = {}
for _ in range(snakes):
    i, j = map(int, input().split())
    snake[i] = j

q = deque([[0, 1]])
while 1:
    cnt, now = q.popleft()
    DP.add(now)
    for dice in range(1, 7):
        next = now + dice
        if next in DP:
            continue
        if next == 100:
            print(cnt+1)
            exit()
        if next in ladder:
            if ladder[next] not in DP:
                q.append([cnt+1, ladder[next]])
        elif next in snake:
            if snake[next] not in DP:
                q.append([cnt+1, snake[next]])
        else:
            q.append([cnt+1, next])