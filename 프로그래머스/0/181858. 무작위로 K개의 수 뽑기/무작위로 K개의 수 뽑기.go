func solution(arr []int, k int) []int {
    result := []int{}
    for _, i := range arr {
        if len(result) == k{
            break
        }
        check := true
        for _, j := range result {
            if i == j {
                check = false
                break
            }
        }
        if check {
            result = append(result, i)
        }
    }
    for len(result) < k {
        result = append(result, -1)
    }
    
    return result
}