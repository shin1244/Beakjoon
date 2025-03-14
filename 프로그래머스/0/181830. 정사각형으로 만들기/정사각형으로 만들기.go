func solution(arr [][]int) [][]int {
    row := len(arr)
    col := len(arr[0])
    
    if row > col {
        d := row - col
        for i := 0; i < d; i++ {
            for idx := range arr {
                arr[idx] = append(arr[idx], 0)
            }
        }
    } else if row < col {
        d := col - row
        slice := make([]int, len(arr[0]))
        for i := 0; i < d; i++ {
            arr = append(arr, slice)
        }
    }
    
    return arr
}