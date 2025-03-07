import "strconv"

func solution(intStrs []string, k int, s int, l int) []int {
    result := []int{}
    for _, val := range intStrs {
        n, _ := strconv.Atoi(val[s:s+l])
        if n > k {
            result = append(result, n)
        }
    }
    return result
}