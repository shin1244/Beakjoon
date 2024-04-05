from collections import deque

n, m = map(int,input().split())

arr = [list(input()) for _ in range(m)]

result = {"W":0, "B":0}

def BFS(y, x, color):
    q = deque([[y, x]])
    count = 1
    while q:
        now_y, now_x = q.popleft()
        for ny, nx in [[1,0],[-1,0],[0,1],[0,-1]]:
            if 0 <= now_y+ny < m and 0 <= now_x+nx < n:
                if arr[now_y+ny][now_x+nx] == color:
                    q.append([now_y+ny, now_x+nx])
                    arr[now_y+ny][now_x+nx] = "N"
                    count += 1
    return 1 if count == 1 else (count-1) ** 2
    

for y in range(m):
    for x in range(n):
        if arr[y][x] != "N":
            result[arr[y][x]] += BFS(y, x, arr[y][x])

print(*result.values())