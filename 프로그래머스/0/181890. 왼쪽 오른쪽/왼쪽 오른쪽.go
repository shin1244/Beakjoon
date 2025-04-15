func solution(str_list []string) []string {
    for idx, val := range str_list {
        if val == "l" {
            return str_list[:idx]
        } else if val == "r" {
            return str_list[idx+1:]
        }
    }
    return []string{}
}