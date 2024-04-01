from collections import deque
import sys
input = sys.stdin.readline

length, width = map(int, input().split())
arr = [list(map(int, input().strip())) for _ in range(length)]
q = deque([[0, 0, 0]])
visited = [[[0] * 2 for _ in range(width)] for _ in range(length)]
visited[0][0][0] = 1

while q:
    y, x, chance = q.popleft()
    if x == width - 1 and y == length - 1:
        print(visited[y][x][chance])
        exit()

    for ny, nx in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
        if 0 <= ny + y < length and 0 <= nx + x < width:
            if arr[ny + y][nx + x] == 0 and visited[ny + y][nx + x][chance] == 0:
                q.append([ny + y, nx + x, chance])
                visited[ny + y][nx + x][chance] = visited[y][x][chance] + 1
            elif arr[ny + y][nx + x] == 1 and chance == 0:
                q.append([ny + y, nx + x, 1])
                visited[ny + y][nx + x][1] = visited[y][x][chance] + 1

print(-1)
