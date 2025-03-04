func solution(n int) [][]int {
    result := [][]int{}
    for i := 0; i < n; i++ {
        jArr := []int{}
        for j := 0; j < n; j++ {
            if i == j {
                jArr = append(jArr, 1)
            } else {
                jArr = append(jArr, 0)
            }
        }
        result = append(result, jArr)
    }
    return result
}