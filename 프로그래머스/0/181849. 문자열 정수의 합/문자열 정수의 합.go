import "strconv"

func solution(num_str string) int {
    result := 0
    for i := 0; i < len(num_str); i++ {
        val, _ := strconv.Atoi(string(num_str[i]))
        result += val
    }
    return result
}