input()
arr = list(map(int,input().split(' ')))
answer = 0
for i in arr:
    if i == 2:
        answer += 1
        continue
    if i % 2 != 0 and i != 1:
        c = 1
        for j in range(3,i//2,2):
            if i % j == 0:
                c = 0
                break
        if c:
            answer += 1
print(answer)