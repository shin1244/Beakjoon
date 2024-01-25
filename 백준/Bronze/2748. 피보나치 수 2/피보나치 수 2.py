n = int(input())
if n == 1:
    print(1)
    exit()

dp1 = [0] * (n+1)
dp1[1], dp1[2] = 1, 1
dp2 = [0] * (n+1)
dp2[1], dp2[2] = 1, 1

def fibo1(n):
    if dp1[n] != 0:
        return dp1[n]
    else:
        dp1[n] = fibo1(n-1) + fibo1(n-2)
        return dp1[n]

#print(fibo1(n))

def fibo2(n):
    for i in range(2,n+1):
        dp2[i] = dp2[i-1] + dp2[i-2]
    return dp2[n]

print(fibo2(n))