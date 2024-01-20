from heapq import *

ax, ay = map(int, input().split())

arr = [input().rstrip() for _ in range(ax)]
visited = [[False] * ay for _ in range(ax)]

h = [[0, 0, 0]]

while h:
    index, x, y = heappop(h)

    if x == ax - 1 and y == ay - 1:
        print(index + 1)
        break

    for nx, ny in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nn, ny = x + nx, y + ny

        if 0 <= nn < ax and 0 <= ny < ay and not visited[nn][ny] and arr[nn][ny] == '1':
            heappush(h, [index + 1, nn, ny])
            visited[nn][ny] = True
