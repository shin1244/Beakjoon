n = int(input())

arr = [list(map(int,input())) for _ in range(n)]

def DFS(b, a, count):
    arr[b][a] = 0
    for y, x in [[1,0],[0,1],[0,-1], [-1,0]]:
        if y+b in range(n) and x+a in range(n):
            if arr[y+b][x+a] == 1:
                count += 1
                count = DFS(y+b, x+a, count)
    return count

def BFS(b, a, count):
    stack = [[b, a]]
    while stack:
        yy, xx =  stack.pop(0)
        if arr[yy][xx] != 1:
            continue
        arr[yy][xx] = 0
        count += 1
        for y, x in [[1,0],[0,1],[0,-1],[-1,0]]:
            if yy+y in range(n) and xx+x in range(n):
                if arr[yy+y][xx+x] == 1:
                    stack.append([yy+y, xx+x])
    return count

result = []
c = -1
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            c -=1
            result.append(BFS(i, j, 0))

print(len(result))
for i in sorted(result):
    print(i)