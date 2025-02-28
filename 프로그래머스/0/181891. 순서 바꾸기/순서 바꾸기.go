func solution(num_list []int, n int) []int {
    result := []int{}
    result = append(result, append(num_list[n:], num_list[:n]...)...)
    return result
}