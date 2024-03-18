n = int(input())

if n == 1:
    print(0)
    exit()
elif n < 4:
    print(1)
    exit()

DP = [0] * (n+1)
DP[1] = 0
DP[2] = 1
DP[3] = 1

for i in range(4, n+1):
    if i % 3 == 0 and i % 2 == 0:
        DP[i] = min((DP[i//3] + 1), (DP[i//2] + 1))
    elif i % 3 == 0:
        DP[i] = min((DP[i//3] + 1), DP[i-1] + 1)
    elif i % 2 == 0:
        DP[i] = min((DP[i//2] + 1), DP[i-1] + 1)
    else:
        DP[i] = DP[i-1] + 1

print(DP[-1])