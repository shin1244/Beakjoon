n = int(input())

result = []
while n != 1:
    c = 1
    for i in range(2,int(n**(0.5))+1):
        if n % i == 0:
            print(i)
            n = n//i
            c = 0
            break
    if c:
        print(n)
        n = 1