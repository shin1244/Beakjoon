func solution(board [][]int, k int) int {
    result := 0
    for i := 0; i < len(board); i++ {
        for j := 0; j < len(board[0]); j++ {
            if i + j <= k {
                result += board[i][j]
            }
        }
    }
    return result
}