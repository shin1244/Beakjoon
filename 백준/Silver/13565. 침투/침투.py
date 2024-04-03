from collections import deque


def BFS(start):
    q = deque([[0,start]])
    visited = set()
    while q:
        y, x = q.popleft()
        if (y, x) in visited:
            continue
        visited.add((y, x))
        for ny, nx in [[1,0],[-1,0],[0,1],[0,-1]]:
            if 0 <= ny+y < n and 0 <= nx+x < m:
                if arr[ny+y][nx+x] == '0':
                    if ny+y == n-1:
                        return True
                    q.append([ny+y, nx+x])
    return False


n, m = map(int,input().split(' '))

arr = [list(input()) for _ in range(n)]

for x in range(m):
    if arr[0][x] == '0' and BFS(x):
        print("YES")
        exit()
        
print("NO")