def solution(priorities, location):
    arr = [[priorities[i], i] for i in range(len(priorities))]
    count = 0
    
    while arr:
        count += 1
        arr = arr[arr.index(max(arr,key=lambda x: x[0])):]+arr[:arr.index(max(arr,key=lambda x: x[0]))]
        print(arr)
        if arr.pop(0)[1] == location:
            return count