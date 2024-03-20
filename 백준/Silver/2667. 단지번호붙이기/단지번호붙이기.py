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

result = []

for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            result.append(DFS(i, j, 1))

print(len(result))
for i in sorted(result):
    print(i)