arr = [int(input()) for _ in range(int(input()))]

def Beakjoon(arr):
    for i in range(1,len(arr)):
        temp = arr[i]
        for j in range(i, -1, -1):
            if arr[j-1] > temp:
                arr[j] = arr[j-1]
            else: break
        arr[j] = temp
    return arr

[print(str) for str in Beakjoon(arr)]