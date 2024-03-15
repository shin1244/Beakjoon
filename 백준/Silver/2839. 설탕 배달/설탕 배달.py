n = int(input())
c = True
for i in range(n//5, -1, -1):
    if (n-5*i) % 3 == 0:
        print(i+(n-5*i)//3)
        c = False
        break

if c:
    print(-1)