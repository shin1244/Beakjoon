func solution(my_string string) []int {
    result := make([]int, 52)
    for _, val := range my_string {
        if 'a' <= val && val <= 'z' {
            result[int(val-'a')+26]++
        } else {
            result[int(val-'A')]++
        }
    }
    return result
}