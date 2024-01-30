N = int(input())

for _ in range(N):
    input()
    coins = map(int,input().split())
    money = int(input())

    DP = [0] * (money+1)
    DP[0] = 1

    for coin in coins:
        for i in range(coin, len(DP)):
            DP[i] += DP[i-coin]
    
    print(DP[-1])