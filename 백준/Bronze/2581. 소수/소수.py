n1 = int(input())
n2 = int(input())

result = 0
answer = 0

for i in range(n1, n2+1):
    c = 1
    if i == 1: continue
    for j in range(2, int(i**(1/2)+1)):
        if i % j == 0:
            c = 0
            break
    if c:
        if answer == 0: answer = i
        result += i

if answer == 0: print(-1)
else:
    print(result)
    print(answer)