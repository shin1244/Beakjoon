import sys
input = sys.stdin.readline

n = int(input())
result = []

for _ in range(n):
    i = input().rstrip().split(" ")
    if i[0] == '1':
        result.append(i[1])
    elif i[0] == '2':
        if result: print(result.pop())
        else: print(-1)
    elif i[0] == '3':
        print(len(result))
    elif i[0] == '4':
        print(0) if len(result) else print(1)
    else:
        if result: print(result[-1])
        else: print(-1)