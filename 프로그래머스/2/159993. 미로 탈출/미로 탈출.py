from collections import deque

def solution(maps):
    result = 0
    for y in range(len(maps)):
        for x in range(len(maps[y])):
            if maps[y][x] == 'S':
                count, now = BFS(y, x, maps, 1)
                if count == -1:
                    return -1
                result += count
                count, now = BFS(now[0], now[1], maps, 0)
                if count == -1:
                    return -1
                result += count
                return result


def BFS(y, x, maps, L):
    n = len(maps)
    m = len(maps[0])
    q = deque([[0,y,x]])
    visited = set()

    while q:
        cnt, now_y, now_x = q.popleft()
        if L == 1 and maps[now_y][now_x] == 'L':
            return (cnt, [now_y, now_x])
        if L == 0 and maps[now_y][now_x] == 'E':
            return (cnt, [now_y, now_x])
        for ny, nx in [[1,0],[-1,0],[0,1],[0,-1]]:
            next_y, next_x = ny+now_y, nx+now_x
            if 0 <= next_y < n and 0 <= next_x < m:
                if maps[next_y][next_x] != 'X' and (next_y, next_x) not in visited:
                    q.append([cnt+1, next_y, next_x])
                    visited.add((next_y, next_x))

    return (-1, -1)