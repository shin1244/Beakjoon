from collections import deque
import sys

input = sys.stdin.readline


n, m = map(int,input().split())
arr = [list(input().rstrip()) for _ in range(n)]
input()
bars = list(map(int,input().rstrip().split(' ')))


def BFS(y, x):
    if y == n-1:
        return True
    visited.add((y,x))
    q = deque([[y,x]])
    while q:
        now_y, now_x = q.popleft()
        if now_y == n-1:
            return False
        for ny, nx in [[0,-1],[0,1],[-1,0],[1,0]]:
            next_y, next_x = now_y+ny, now_x+nx
            if 0 <= next_y < n and 0 <= next_x < m:
                if arr[next_y][next_x] == 'x' and (next_y, next_x) not in visited:
                    visited.add((next_y, next_x))
                    q.append([next_y, next_x])
    return visited


def down(s):
    dic = {}
    for y, x in s:
        if x in dic:
            dic[x].append(y)
        else:
            dic[x] = [y]
    min_length = 999
    for x in dic:
        c = 1
        for i in dic[x]:
            for y in range(i+1, n):
                if arr[y][x] == 'x' and (y, x) not in s:
                    min_length = min(min_length, y-i-1)
                    c = 0
                    break
            if c:
                min_length = min(min_length, n-i-1)
    result = set()
    for y, x in s:
        arr[y][x] = '.'
        result.add((y+min_length, x))
    for y, x in result:
        arr[y][x] = 'x'


for bar in range(len(bars)):
    now = n-bars[bar]
    repeat = range(m) if bar % 2 == 0 else range(m-1, -1, -1)
    for i in repeat:
        if arr[now][i] == 'x':
            arr[now][i] = '.'
            for y, x in [[0,-1],[0,1],[-1,0],[1,0]]:
                next_y, next_x = now+y, i+x
                if 0 <= next_y < n and 0 <= next_x < m:
                    if arr[next_y][next_x] == 'x':
                        visited = set()
                        fall = BFS(next_y, next_x)
                        if type(fall) == set:
                            down(fall)
            break

for i in arr:
    print(''.join(i))