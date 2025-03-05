func solution(a int, d int, included []bool) int {
    result := 0
    for i, b := range included {
        if b {
            result += a + i* d
        }
    }
    return result
}