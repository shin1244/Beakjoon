func solution(n int) int64 {
    DP := make([]int, n+1)
    DP[0] = 1
    DP[1] = 1
    
    for i := 2; i <= n; i++ {
        DP[i] = DP[i-1] % 1234567 + DP[i-2] % 1234567
    }
    
    return int64(DP[n]) % int64(1234567)
}