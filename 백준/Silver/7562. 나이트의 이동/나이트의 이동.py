from collections import deque

n = int(input())
for i in range(n):
    borad = int(input())
    knight_y, knight_x = map(int,input().split(' '))
    goal_y, goal_x = map(int,input().split(' '))

    s = [[0] * borad for _ in range(borad)]

    q = deque([[knight_y, knight_x, 0]])
    while q:
        y, x, cnt = q.popleft()
        s[y][x] = 1
        if y == goal_y and x == goal_x:
            print(cnt)
            break

        for move in [[2,1],[1,2]]:
            for now in [[1,1],[-1,1],[1,-1],[-1,-1]]:
                ny, nx = move[0]*now[0]+y, move[1]*now[1]+x
                if 0 <= ny < borad and 0 <= nx < borad and s[ny][nx] == 0:
                        s[ny][nx] = 1
                        q.append([ny, nx, cnt+1])