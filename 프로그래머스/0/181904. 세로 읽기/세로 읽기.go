func solution(my_string string, m int, c int) string {
    result := ""
    for i := c-1; i < len(my_string); i += m {
        result += string(my_string[i])
    }
    return result
}