func solution(my_string string, overwrite_string string, s int) string {
    result := my_string[:s] + overwrite_string
    if s + len(overwrite_string) < len(my_string) {
        result += my_string[s+len(overwrite_string):]
    }
    return result
}