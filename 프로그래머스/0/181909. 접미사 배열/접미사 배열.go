func solution(my_string string) []string {
    result := []string{}
    for i := len(my_string)-1; i >= 0; i-- {
        result = append(result, my_string[i:])
    }
    for i := 1; i < len(result); i++ {
        key := result[i]
        j := i - 1
        for j >= 0 && result[j] > key {
            result[j+1] = result[j]
            j--
        }
        result[j+1] = key
    }
    return result
}