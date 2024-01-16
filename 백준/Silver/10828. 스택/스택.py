n = int(input())
arr = [input().split() for _ in range(n)]

arrEmpty = [None] * n
index = -1
for item in arr:
    if item[0] == 'push':
        index += 1
        arrEmpty[index] = item[1]
    elif item[0] == 'pop':
        if index == -1:
            print(-1)
        else:
            print(arrEmpty[index])
            index -= 1
    elif item[0] == 'size':
        print(index+1)
    elif item[0] == 'empty':
        print(1) if index == -1 else print(0)
    elif item[0] == 'top':
        if index == -1:
            print(-1)
        else:
            print(arrEmpty[index])