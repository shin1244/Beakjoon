from collections import deque

def solution(land):
    row = len(land[0])
    column = len(land)
    DP = [0] * row
    for x in range(row):
        for y in range(column):
            if land[y][x] == 1:
                q = deque([[y,x]])
                visited = set()
                count = 0
                while q:
                    now_y, now_x = q.popleft()
                    visited.add((now_y, now_x))
                    count += 1
                    
                    for ny, nx in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                        new_y, new_x = now_y + ny, now_x + nx
                        if 0 <= new_y < column and 0 <= new_x < row:
                            if (new_y, new_x) not in visited and land[new_y][new_x] == 1:
                                land[new_y][new_x] = 0
                                q.append([new_y, new_x])
                row_check = set()
                for _, vx in visited:
                    row_check.add(vx)
                for check in row_check:
                    DP[check] += len(visited)
                    
    return max(DP)