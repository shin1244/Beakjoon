func solution(str1 string, str2 string) string {
    result := ""
    for idx := range str1 {
        result += string(str1[idx])
        result += string(str2[idx])
    }
    return result
}