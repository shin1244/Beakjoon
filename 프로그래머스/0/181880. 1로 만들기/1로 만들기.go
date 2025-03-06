func solution(num_list []int) int {
    result := 0
    for _, val := range num_list {
        for val != 1 {
            result++
            if val % 2 == 1 {
                val--
            }
            val /= 2
        }
    }
    return result
}