func solution(arr []int) []int {
    stk := []int{}
    i := 0
    
    for i < len(arr) {
        if len(stk) == 0{
            stk = append(stk, arr[i])
            i++
        } else if stk[len(stk)-1] < arr[i] {
            stk = append(stk, arr[i])
            i++
        } else {
            stk = stk[:len(stk)-1]
        }
    }
    return stk
}