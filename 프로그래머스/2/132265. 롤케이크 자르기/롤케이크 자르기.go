func solution(topping []int) int {
    left := make(map[int]int)
    right := make(map[int]int)
    result := 0
    
    for _, val := range topping {
        right[val]++
    }
    
    for _, val := range topping {
        left[val]++
        right[val]--
        
        if right[val] == 0 {
            delete(right, val)
        }
        if len(right) == len(left) {
            result++
        }
    }
    return result
}