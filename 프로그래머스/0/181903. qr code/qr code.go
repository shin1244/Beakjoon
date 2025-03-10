func solution(q int, r int, code string) string {
    result := ""
    for idx := range code {
        if idx % q == r {
            result += string(code[idx])
        }
    }
    return result
}