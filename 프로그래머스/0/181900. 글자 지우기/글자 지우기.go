func solution(my_string string, indices []int) string {
    result := ""
    for i := range my_string {
        c := true
        for _, val := range indices {
            if i == val {
                c = false
                break
            }
        }
        if c {
            result += string(my_string[i])
        }
    }
    return result
}