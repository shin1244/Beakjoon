def solution(N, number):
    if N == number:
        return 1
    DP = [set() for i in range(8)]
    for i in range(1,9):
        DP[i-1].add(int(str(N)*i))
    
    
    for i in range(1, 8):
        for j in range(i):
            for a in DP[j]:
                for b in DP[i-j-1]:
                    DP[i].update([a+b, a-b, a*b])
                    if a and b: DP[i].add(a//b)
        if number in DP[i]:
            return i + 1
    return -1