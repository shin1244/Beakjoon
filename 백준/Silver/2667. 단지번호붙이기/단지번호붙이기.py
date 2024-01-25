from collections import deque

n = int(input())

arr = [list(map(int,list(input()))) for _ in range(n)]

result = []
for i in range(n):
    for j in range(n):
        if arr[i][j] != 0:
            q = deque([(i,j)])
            c = 0
            visited = set([(i,j)])
            while q:
                y,x = q.popleft()
                if arr[y][x] == 1:
                    arr[y][x] = 0
                    c += 1
                for py, px in [[1,0],[-1,0],[0,1],[0,-1]]:
                    now_y, now_x = y+py, x+px
                    if (now_y, now_x) not in visited:
                        if 0<=now_y<n and 0<=now_x<n and arr[now_y][now_x] == 1:
                            visited.add((now_y, now_x))
                            q.append((now_y, now_x))
            
            result.append(c)

print(len(result))
result.sort()
for i in result:
    print(i)