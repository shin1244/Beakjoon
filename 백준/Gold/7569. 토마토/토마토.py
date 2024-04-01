from collections import deque
import sys
input = sys.stdin.readline

width, length, height = map(int,input().split(' '))

arr = [[list(map(int,input().split(' '))) for _ in range(length)] for _ in range(height)]
tomato = deque()


for h in range(height):
    for y in range(length):
        for x in range(width):
            if arr[h][y][x] == 1:
                tomato.append([h,y,x,0])

while tomato:
    h, y, x, cnt = tomato.popleft()
    for nh,ny,nx in [[1,0,0],[-1,0,0],[0,1,0],[0,-1,0],[0,0,1],[0,0,-1]]:
        if 0 <= h+nh < height and 0 <= y+ny < length and 0 <= x+nx < width:
            if arr[h+nh][y+ny][x+nx] == 0:
                arr[h+nh][y+ny][x+nx] = 1
                tomato.append([h+nh, y+ny, x+nx, cnt+1])

                

for i in arr:
    for j in i:
        if 0 in j:
            print(-1)
            exit()

print(cnt)