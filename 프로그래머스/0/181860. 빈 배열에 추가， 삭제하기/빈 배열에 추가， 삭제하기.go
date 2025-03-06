func solution(arr []int, flag []bool) []int {
    result := []int{}
    for idx := range arr {
        if flag[idx] {
            for i := 0; i < arr[idx] * 2; i++ {
                result = append(result, arr[idx])
            }
        } else {
            result = result[:len(result)-arr[idx]]
        }
    }
    return result
}