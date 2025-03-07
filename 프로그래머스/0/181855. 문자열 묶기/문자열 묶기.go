func solution(strArr []string) int {
    dict := make(map[int]int)
    result := 0
    for _, val := range strArr {
        dict[len(val)]++
    }
    for _, val := range dict {
        if val > result {
            result = val
        }
    }
    return result
}