func solution(num_list []int) int {
    for idx, val := range num_list {
        if val < 0 {
            return idx
        }
    }
    return -1
}