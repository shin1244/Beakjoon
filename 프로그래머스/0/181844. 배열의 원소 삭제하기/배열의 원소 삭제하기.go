func solution(arr []int, delete_list []int) []int {
    result := []int{}
    for i := range arr {
        c := true
        for j := range delete_list {
            if arr[i] == delete_list[j] {
                c = false
                break
            }
        }
        if c {
            result = append(result, arr[i])
        }
    }
    
    return result
}