N = int(input())
if N % 2:
    print(0)
    exit()

DP = [0] * (N + 1)
DP[0] = 1
DP[2] = 3

for i in range(4, N+1, 2):
    DP[i] = DP[i-2] * 3
    for j in range(4, i+1, 2):
        DP[i] += DP[i-j] * 2
        

print(DP[N]) 