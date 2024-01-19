import sys
from collections import deque, defaultdict
input = sys.stdin.readline
total, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
arr_dict = defaultdict(list)
for key1, key2 in arr:
    arr_dict[key1].append(key2)
    arr_dict[key2].append(key1)
visited = set()
component_count = 0
for i in range(1, total + 1):
    if i not in visited:
        if i in arr_dict:
            q = deque([i])
            while q:
                now = q.popleft()
                if now not in visited:
                    q.extend(arr_dict[now])
                    visited.add(now)
        component_count += 1
print(component_count)