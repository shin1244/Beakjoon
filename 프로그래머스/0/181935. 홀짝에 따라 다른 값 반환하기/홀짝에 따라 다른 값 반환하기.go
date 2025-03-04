func solution(n int) int {
    result := 0
    for i := n; i > 0; i-=2 {
        if n % 2 == 0 {
            result += i * i
        } else {
            result += i
        }
    }
    return result
}