func solution(picture []string, k int) []string {
    result := []string{}
    for _, str := range picture {
        temp := ""
        for _, val := range str {
            for i := 0; i < k; i++ {
                temp += string(val)
            }
        }
        for i := 0; i < k; i++ {
            result = append(result, temp)
        }
    }
    return result
}