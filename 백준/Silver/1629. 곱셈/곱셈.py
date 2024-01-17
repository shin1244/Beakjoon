a, b, c = list(map(int,input().split(' ')))

def fast_expo(num, power, mod):
    result = 1
    num = num % mod

    while power > 0:
        if power % 2 == 1:
            result = (result * num) % mod
        power //= 2
        num = (num * num) % mod

    return result

print(fast_expo(a,b,c))