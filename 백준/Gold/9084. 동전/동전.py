n = int(input())

for _ in range(n):

    
    now_n = int(input())
    arr = list(map(int,input().split(' ')))
    money = int(input())

    DP = [0] * (money + 1)
    DP[0] = 1

    for i in arr:
        for j in range(1,money+1):
            if j >= i:
                DP[j] += DP[j-i]

    print(DP[-1])