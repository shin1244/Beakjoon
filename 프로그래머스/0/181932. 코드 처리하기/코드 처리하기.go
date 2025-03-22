func solution(code string) string {
    result := ""
    mode := 0
    for idx := range code {
        if string(code[idx]) == "1" {
            mode = 1 - mode
        } else {
            if idx % 2 == mode {
                result += string(code[idx])
            }
        }
    }
    if result == "" {
        return "EMPTY"
    }
    return result
}