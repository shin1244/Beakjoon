from collections import deque

def solution(board):
    m = len(board)
    n = len(board[0])
    q = deque()

    for y in range(m):
        for x in range(n):
            if board[y][x] == "R":
                q.append([y,x,0])
                break

    
    visited = []
    while q:
        now = q.popleft()
        if board[now[0]][now[1]] == "G":
            return now[2]
        for next in [[-1,0],[1,0],[0,-1],[0,1]]:
            dest = goStraight(board, now[:2], next)
            if dest not in visited:
                q.append(dest + [now[2]+1])
                visited.append(dest)
    
    return -1


    
def goStraight(board, nowPos, direction):
    m = len(board)
    n = len(board[0])
    y, x = nowPos

    while True:
        ny = y + direction[0]
        nx = x + direction[1]

        if not (0 <= ny < m and 0 <= nx < n):
            break
        if board[ny][nx] == "D":
            break

        y, x = ny, nx

    return [y, x]