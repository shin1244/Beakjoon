func solution(l int, r int) []int {
    result := []int{}
    for i := l; i <= r; i++ {
        num := i
        check := true
        for num > 10 {
            if num % 10 != 5 && num % 10 != 0 {
                check = false
                break
            }
            num /= 10
        }
        if check && (num == 0 || num == 5) {
            result = append(result, i)
        }
    }
    if len(result) == 0 {
        return []int{-1}
    }
    return result
}