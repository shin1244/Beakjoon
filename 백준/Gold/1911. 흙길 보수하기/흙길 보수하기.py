n, m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]

arr = sorted(arr)
end = arr[-1][-1]

now, result = 0, 0
while now < end:
    water_start, water_end = arr.pop(0)
    now = max(water_start, now)
    
    need_bar = (water_end - now) // m
    if (water_end - now) % m:
        need_bar += 1
    result += need_bar
    now = need_bar * m + now

print(result)