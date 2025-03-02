func solution(my_string string, is_suffix string) int {
    if len(is_suffix) > len(my_string) {
        return 0
    } else if my_string[len(my_string)-len(is_suffix):] == is_suffix {
        return 1
    }
    return 0
}