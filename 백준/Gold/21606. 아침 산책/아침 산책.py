n = int(input())
route = input()
route = {i:int(route[i-1]) for i in range(1, n+1)}
arr = [list(map(int,input().split())) for _ in range(n-1)]


route_dict = {}
for i, j in arr:
    if i in route_dict:
        route_dict[i].append(j)
    else:
        route_dict[i] = [j]
    if j in route_dict:
        route_dict[j].append(i)
    else:
        route_dict[j] = [i]

def dfs(start, inout):
    if start in visited:
        return 0
    result = 0
    inout += route[start]
    visited.add(start)
    if inout == 1:
        return 1
    for i in route_dict[start]:
        result += dfs(i, inout)
    return result

answer = 0
for i in route:
    if route[i]:
        visited = set()
        answer += dfs(i, -1)

print(answer)