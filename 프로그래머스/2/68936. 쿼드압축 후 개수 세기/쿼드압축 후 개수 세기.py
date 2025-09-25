def solution(arr):
    check = []
    for i in arr:
        check.extend(i)
    
    if len(set(check)) == 1:
        if check[0] == 0:
            return [1,0]
        else:
            return [0,1]
    else:
        n = len(arr) // 2
        a = solution([row[:n] for row in arr[:n]])
        b = solution([row[n:] for row in arr[:n]])
        c = solution([row[:n] for row in arr[n:]])
        d = solution([row[n:] for row in arr[n:]])
        return [a[0]+b[0]+c[0]+d[0], a[1]+b[1]+c[1]+d[1]]