n = int(input())

result = [0,0,0]

result[0] += n // 300
n = n % 300
result[1] += n // 60
n = n % 60
result[2] += n // 10
n = n % 10
if n:
    print(-1)
else:
    print(*result)