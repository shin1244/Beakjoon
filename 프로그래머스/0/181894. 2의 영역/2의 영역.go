func solution(arr []int) []int {
    s := 0
    e := len(arr)-1
    for s < len(arr) && arr[s] != 2 {
        s++
    }
    for e > 0 && arr[e] != 2  {
        e--
    }
    
    if s > e {
        return []int{-1}
    }
    
    return arr[s:e+1]
}