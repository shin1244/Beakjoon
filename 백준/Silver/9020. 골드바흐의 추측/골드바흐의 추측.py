def if_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True


N = int(input())
for _ in range(N):
    num = int(input())
    for i in range(num//2, 1, -1):
        if if_prime(i) and if_prime(num - i):
            print(i, num - i)
            break