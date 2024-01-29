def solution(t):
    DP = [[] for i in range(len(t))]
    DP[0] = t[0]
    
    for i in range(1,len(t)):
        now_arr = t[i]
        for j in range(len(now_arr)):
            if j == 0:
                DP[i].append(now_arr[j]+DP[i-1][j])
            elif j == len(now_arr)-1:
                DP[i].append(now_arr[j]+DP[i-1][j-1])
            else:
                DP[i].append(max(now_arr[j]+DP[i-1][j], 
                                 now_arr[j]+DP[i-1][j-1]))
    
    return max(DP[-1])