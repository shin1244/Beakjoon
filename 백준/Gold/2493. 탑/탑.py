n = int(input())
arr = list(map(int, input().split(' ')))
result = [-1] * n  # 초기값을 -1로 설정
stack = []

for i in range(n):
    a = 0
    while stack and arr[i] > arr[stack[-1]]:
        stack.pop()
    if stack:
        result[i] = stack[-1]+1
    else:
        result[i] = 0
    stack.append(i)


for i in range(n):
    print(result[i], end=' ')
