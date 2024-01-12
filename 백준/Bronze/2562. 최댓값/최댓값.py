def Beakjoon(num):
    result = [0, 0]
    for i in range(len(num)):
        if result[0] < num[i]:
            result = [num[i], i+1]
    
    print(result[0])
    print(result[1])

A = [int(input()) for i in range(9)]
Beakjoon(A)