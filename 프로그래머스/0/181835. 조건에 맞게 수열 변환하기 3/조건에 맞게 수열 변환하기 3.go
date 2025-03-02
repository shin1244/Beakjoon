func solution(arr []int, k int) []int {
    result := []int{}
    for _, v := range arr {
        if k % 2 == 1 {
            result = append(result, v * k)
        } else {
            result = append(result, v + k)
        }
    }
    return result
}