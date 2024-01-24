com = int(input())
edges = int(input())

arr = [list(map(int,input().split())) for _ in range(edges)]

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

result = 0
visited = set()
def DFS(start):
    global result
    if start not in visited:
        result += 1
        visited.add(start)
        if start in graph_dict:
            for i in graph_dict[start]:
                DFS(i)

DFS(1)
print(result-1)