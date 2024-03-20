n, m = map(int,input().split(' '))
coin = [int(input()) for _ in range(n)]

DP = [0] * (m+1)
DP[0] = 1

for i in coin:
    for j in range(i, m+1):
        DP[j] += DP[j-i]

print(DP[-1])