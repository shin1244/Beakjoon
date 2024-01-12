for i in range(int(input())):
    n, s = input().split(' ')
    n = int(n)
    print(''.join([i*n for i in s]))