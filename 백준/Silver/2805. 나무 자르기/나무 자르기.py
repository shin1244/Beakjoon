need = int(input().split(' ')[1])
trees = list(map(int,input().split(' ')))

start, end = 1, max(trees)

while start <= end:
    result = 0
    mid = (start + end) // 2
    for i in trees:
        if i > mid:
            result += i - mid
    
    if result < need:
        end = mid - 1
    else:
        start = mid + 1
        
print(end)