from collections import deque

total, n = list(map(int,input().split(' ')))
arr = [list(map(int,input().split(' '))) for _ in range(n)]

graph_dict = {}
for i, j in arr:
    if i in graph_dict:
        graph_dict[i].append(j)
    else:
        graph_dict[i] = [j]

topo_dict = {i:0 for i in range(1,total+1)}

for i in graph_dict:
    for j in graph_dict[i]:
        topo_dict[j] += 1

q = deque()

for i in range(1, total+1):
    if topo_dict[i] == 0:
        q.append(i)

while q:
    now = q.popleft()
    print(now)
    del topo_dict[now]
    if now in graph_dict:
        for i in graph_dict[now]:
            topo_dict[i] -= 1
            if topo_dict[i] == 0:
                q.append(i)