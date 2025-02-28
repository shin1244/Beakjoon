func solution(arr []int) []int {
    for idx, val := range arr {
        if val >= 50 && val % 2 == 0 {
            arr[idx] = val / 2
        } else if val < 50 && val % 2 == 1 {
            arr[idx] = val * 2
        }
    }
    return arr
}