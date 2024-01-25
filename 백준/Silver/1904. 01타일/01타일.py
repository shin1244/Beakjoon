N = int(input())

DP = [0] * (N+1)
if N < 2:
    print(N)
    exit()
DP[1], DP[2] = 1, 2


def zeroOne1(N):
    if DP[N] != 0:
        return DP[N]
    else:
        DP[N] = zeroOne1(N-1) + zeroOne1(N-2)
        return DP[N] % 15746
    
def zeroOne2(N):
    for i in range(3, N+1):
        DP[i] = (DP[i-1] + DP[i-2]) % 15746
    return DP[N] % 15746

print(zeroOne2(N))