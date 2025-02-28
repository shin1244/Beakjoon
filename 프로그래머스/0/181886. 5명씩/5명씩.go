func solution(names []string) []string {
    result := []string{}
    for idx, val := range names {
        if (idx) % 5 == 0 {
            result = append(result, val)
        }
    }
    return result
}