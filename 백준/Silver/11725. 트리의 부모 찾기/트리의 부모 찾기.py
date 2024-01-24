n = int(input())

arr = [list(map(int,input().split())) for _ in range(n-1)]

result = {i:i for i in range(2,n+1)}


graph_dict = {}

for i, j in arr:
    if i in graph_dict:
        graph_dict[i].append(j)
    else:
        graph_dict[i] = [j]
    if j in graph_dict:
        graph_dict[j].append(i)
    else:
        graph_dict[j] = [i]

stack = [1]
visited = set()

while stack:
    now = stack.pop()
    if now not in visited:
        visited.add(now)
        for i in graph_dict[now]:
            if i not in visited:
                result[i] = now
                stack.append(i)


[print(i) for i in result.values()]