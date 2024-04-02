from collections import deque

n, m = map(int, input().split(' '))

yard = [list(input()) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

def BFS(a, b):
    sheep = 0
    wolf = 0
    q = deque()
    q.append([a, b])
    while q:
        y, x = q.popleft()
        if yard[y][x] == "v":
            wolf += 1
        elif yard[y][x] == "o":
            sheep += 1
        visited[y][x] = True
        for ny, nx in [[1,0],[-1,0],[0,-1],[0,1]]:
            next_y, next_x = ny+y, nx+x
            if 0 <= next_y < n and 0 <= next_x < m:
                if not visited[next_y][next_x] and yard[next_y][next_x] != '#':
                    q.append([next_y, next_x])
                    visited[next_y][next_x] = True
    if sheep > wolf:
        result[0] += sheep
    else:
        result[1] += wolf

result = [0,0]

for y in range(n):
    for x in range(m):
        if not visited[y][x] and (yard[y][x] == 'o' or yard[y][x] == 'v'):
            BFS(y, x)

print(*result)
