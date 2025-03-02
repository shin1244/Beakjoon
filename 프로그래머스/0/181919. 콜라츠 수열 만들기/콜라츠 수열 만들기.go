func solution(n int) []int {
    result := []int{}
    for n != 1 {
        result = append(result, n)
        if n % 2 == 0 {
            n /= 2
        } else {
            n = n * 3 + 1
        }
    }
    result = append(result, 1)
    return result
}