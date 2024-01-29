def solution(N, number):
    if N == number:
        return 1
    DP = [set() for _ in range(8)]
    for i in range(8):
        DP[i].add(int(str(N) * (i+1)))
    
    for i in range(1,8):
        for j in range(i):
            for op1 in DP[j]:
                for op2 in DP[i-j-1]:
                    DP[i].add(op1+op2)
                    DP[i].add(op1-op2)
                    DP[i].add(op1*op2)
                    if op2 != 0:
                        DP[i].add(op1//op2)
        if number in DP[i]:
            return i+1
    return -1