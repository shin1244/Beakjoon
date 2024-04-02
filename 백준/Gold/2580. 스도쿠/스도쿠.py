arr = [list(map(int,input().split(' '))) for _ in range(9)]
numbers = []

def col(x, n):
    for i in range(9):
        if arr[i][x] == n:
            return False
    return True

def row(y, n):
    for i in range(9):
        if arr[y][i] == n:
            return False
    return True

def square(y, x, n):
    ny = 3*(y//3)
    nx = 3*(x//3)
    for i in range(ny, ny+3):
        for j in range(nx, nx+3):
            if arr[i][j] == n:
                return False
    return True

def sodoku(start):
    if start == len(numbers):
        for i in arr:
            print(*i)
        exit()
    
    for i in range(1,10):
        y, x = numbers[start][0], numbers[start][1]
        if row(y, i) and col(x, i) and square(y, x, i):
            arr[y][x] = i
            sodoku(start + 1)
            arr[y][x] = 0

for y in range(9):
    for x in range(9):
        if arr[y][x] == 0:
            numbers.append([y,x])

sodoku(0)