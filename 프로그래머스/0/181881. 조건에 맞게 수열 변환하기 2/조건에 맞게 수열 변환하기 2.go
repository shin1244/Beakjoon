func solution(arr []int) int {
    temp := make([]int, len(arr))
    result := 0
    
    for {
        copy(temp, arr)
        
        for idx := range arr {
            if arr[idx] >= 50 && arr[idx] % 2 == 0 {
                arr[idx] /= 2
            } else if arr[idx] < 50 && arr[idx] % 2 == 1 {
                arr[idx] = arr[idx] * 2 + 1
            }
        }
        
        
        check := true
        
        for idx := range arr {
            if arr[idx] != temp[idx] {
                check = false
                break
            }
        }
        if check {
            break
        }
        result++
    }

    return result
}