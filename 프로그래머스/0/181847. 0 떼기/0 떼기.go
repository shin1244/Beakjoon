func solution(n_str string) string {
    for n_str[0] == '0' {
        n_str = n_str[1:]
    }
    return n_str
}