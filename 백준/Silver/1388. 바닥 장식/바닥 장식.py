ay, ax = list(map(int,input().split()))
arr = [list(input()) for i in range(ay)]

visited = set()

def DFS(y,x,a):
    if y < ay and x < ax:
        if (y,x) not in visited:
            if arr[y][x] == '-' and arr[y][x] == a:
                DFS(y,x+1,a)
            elif arr[y][x] == '|' and arr[y][x] == a:
                DFS(y+1,x,a)
            else: return
            visited.add((y,x))

result = 0
for i in range(ay):
    for j in range(ax):
        if (i,j) not in visited:
            DFS(i,j,arr[i][j])
            result += 1

print(result)