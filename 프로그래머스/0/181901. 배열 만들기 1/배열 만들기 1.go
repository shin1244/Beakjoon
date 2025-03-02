func solution(n int, k int) []int {
    result := []int{}
    for i := k; i <= n; i+=k {
        result = append(result, i)
    }
    return result
}