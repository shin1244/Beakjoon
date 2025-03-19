func solution(arr []int, query []int) []int {
    for idx, val := range query {
        if idx % 2 == 0 {
            arr = arr[:val+1]
        } else {
            arr = arr[val:]
        }
    }
    
    return arr
}