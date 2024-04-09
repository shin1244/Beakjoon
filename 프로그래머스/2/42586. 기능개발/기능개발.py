def solution(progresses, speeds):
    arr = [i for i in zip(progresses, speeds)]
    result = []
    while arr:
        arr = [[i+j, j] for i,j in arr]
        count = 0
        while arr and arr[0][0] >= 100:
            count += 1
            arr.pop(0)
        if count:
            result.append(count)
        
    return result