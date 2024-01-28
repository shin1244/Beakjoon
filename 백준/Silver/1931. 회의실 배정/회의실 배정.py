N = int(input())

time = [list(map(int, input().split(' '))) for _ in range(N)]

time.sort(key=lambda x: (x[1],x[0]))

last_time = 0
result = 0
for i in range(N):
    if time[i][0] >= last_time:
        last_time = time[i][1]
        result += 1

print(result)