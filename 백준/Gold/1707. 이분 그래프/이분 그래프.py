import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())

def dfs(start, visited, group):
    visited[start] = group

    for i in graph[start]:
        if visited[i] == 0:
            if not dfs(i, visited, -group):
                return False
        else:
            if visited[i] == group:
                return False
    return True

for _ in range(n):
    nodes, edges = list(map(int,input().split(' ')))
    graph = [[]for _ in range(nodes+1)]
    visited = [0] * (nodes+1)
    for _ in range(edges):
        a,b = list(map(int,input().split(' ')))
        graph[a].append(b)
        graph[b].append(a)
    for i in range(1, nodes+1):
        if visited[i] == 0:
            result = dfs(i, visited, 1)
            if not result:
                break

    print('YES') if result else print('NO')