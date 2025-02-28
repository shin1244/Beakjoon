func solution(num_list []int, n int) []int {
    result := []int{}
    for idx, val := range num_list {
        if idx % n == 0 {
            result = append(result, val)
        }
    }
    return result
}