from collections import deque
import sys
input = sys.stdin.readline

width, length = map(int,input().split(' '))

arr = [list(map(int,input().split(' '))) for _ in range(length)]
tomato = deque()
sample = []
cnt = 0

for y in range(length):
    for x in range(width):
        if arr[y][x] == 1:
            tomato.append([y, x])

while tomato:
    y, x = tomato.popleft()
    for ny, nx in [[1,0],[0,1],[-1,0],[0,-1]]:
        if y+ny in range(length) and x+nx in range(width):
            if arr[y+ny][x+nx] == 0:
                arr[y+ny][x+nx] = 1
                sample.append([y+ny, x+nx])

    if not tomato:
        cnt += 1
        tomato.extend(sample)
        sample = []

for i in arr:
    if 0 in i:
        print(-1)
        exit()
print(cnt-1)