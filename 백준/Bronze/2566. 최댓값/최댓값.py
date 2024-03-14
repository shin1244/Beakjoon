arr = [list(map(int,input().split(' '))) for _ in range(9)]

max_num = -1
answer = []

for i in range(9):
    for j in range(9):
        if arr[i][j] > max_num: 
            answer = [i+1, j+1]
            max_num = arr[i][j]

print(max_num)
print(answer[0], answer[1])