func solution(number []int) int {
    result := 0
    for len(number) > 2 {
        n := number[0]
        number = number[1:]
        for i := 0; i < len(number); i++ {
            for j := i+1; j < len(number); j++ {
                if n + number[i] + number[j] == 0 {
                    result++
                }
            }
        }
    }
    return result
}