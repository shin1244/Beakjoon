func solution(keyinput []string, board []int) []int {
    result := make([]int, 2)
    for _, key := range keyinput {
        switch key {
            case "left":
            if -(board[0]/2) < result[0] {
                result[0]--
            }
            case "right":
            if board[0]/2 > result[0] {
                result[0]++
            }
            case "down":
            if -(board[1]/2) < result[1] {
                result[1]--
            }
            case "up":
            if board[1]/2 > result[1] {
                result[1]++
            }
        }
    }
    return result
}