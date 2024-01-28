import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
for _ in range(N):
    check_arr = [1e9]
    arr = [list(map(int, input().split(' '))) for _ in range(int(input()))]
    arr.sort(key=lambda x: x[0])
    arr = deque(arr)
    while arr:
        now = arr.popleft()
        if now[-1] < check_arr[-1]:
            check_arr.append(now[-1])
    print(len(check_arr)-1)