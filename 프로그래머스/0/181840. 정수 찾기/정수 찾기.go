func solution(num_list []int, n int) int {
    for _, val := range num_list {
        if n == val {
            return 1
        }
    }
    return 0
}