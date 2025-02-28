func solution(todo_list []string, finished []bool) []string {
    result := []string{}
    
    for idx, val := range todo_list {
        if !finished[idx] {
            result = append(result, val)
        }
    }
    return result
}