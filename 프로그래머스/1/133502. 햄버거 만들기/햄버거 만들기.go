func solution(ingredient []int) int {
    temp := []int{}
    result := 0
    for _, val := range ingredient {
        temp = append(temp, val)
        if len(temp) >= 4 {
            match := true
            target := []int{1, 2, 3, 1}
            for i := 0; i < 4; i++ {
                if temp[len(temp)-4+i] != target[i] {
                    match = false
                    break
                }
            }
            if match {
                result++
                temp = temp[:len(temp)-4]
            }
        }
    }
    return result
}
