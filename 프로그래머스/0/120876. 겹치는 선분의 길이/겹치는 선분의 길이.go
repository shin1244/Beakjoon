func solution(lines [][]int) int {
    result := 0
    linesMap := make(map[int]bool)
    
    for idx := range lines{
        for i := lines[idx][0]; i < lines[idx][1]; i++ {
            if linesMap[i] {
                linesMap[i] = false
                result++
            } else {
                linesMap[i] = true
            }
        }
    }
    
    return result
}