func solution(start_num int, end_num int) []int {
    result := []int{}
    for i := start_num; i <= end_num; i++ {
        result = append(result, i)
    }
    return result
}