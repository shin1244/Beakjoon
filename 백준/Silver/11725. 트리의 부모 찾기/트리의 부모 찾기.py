n = int(input())
arr = [list(map(int,input().split())) for _ in range(n-1)]

arr_dict = {}
for i in arr:
    key1 = i[0]
    key2 = i[1]

    if key1 in arr_dict:
        arr_dict[key1].append(key2)
    else:
        arr_dict[key1] = [key2]

    if key2 in arr_dict:
        arr_dict[key2].append(key1)
    else:
        arr_dict[key2] = [key1]
result = {i:0 for i in range(2,n+1)}

def dfs(start):
    visited = set()
    stack= []
    stack.append(start)
    while stack:
        now = stack.pop()
        if now not in visited:
            visited.add(now)
            for i in arr_dict[now]:
                if i not in visited:
                    result[i] = now
                    stack.append(i)

    
dfs(1)
for i in result.values():
    print(i)