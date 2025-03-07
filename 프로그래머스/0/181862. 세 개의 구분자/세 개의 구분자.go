func solution(myStr string) []string {
    result := []string{}
    s := ""
    for _, ch := range myStr {
        if ch == 'a' || ch == 'b' || ch == 'c' {
            if s != "" {
                result = append(result, s)
                s = ""
            }
        } else {
            s += string(ch)
        }
    }
    if s != "" {
        result = append(result, s)
    }
    if len(result) == 0 {
        result = append(result, "EMPTY")
    }
    return result
}