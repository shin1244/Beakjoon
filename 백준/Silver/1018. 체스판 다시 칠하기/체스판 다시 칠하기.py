m,n = map(int,input().split(' '))

board = [list(input()) for _ in range(m)]
result = []

for y in range(m-7):
    for x in range(n-7):
        W = 0
        B = 0
        for i in range(y, y+8):
            for j in range(x, x+8):
                if (i+j)%2 == 0:
                    if board[i][j] == "W":
                        B += 1
                    else:
                        W += 1
                else:
                    if board[i][j] == "W":
                        W += 1
                    else:
                        B += 1
        result.append(W)
        result.append(B)

print(min(result))