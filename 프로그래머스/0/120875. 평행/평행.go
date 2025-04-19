func solution(dots [][]int) int {
    for i := 1; i < 4; i++ {
        x1 := dots[i][0] - dots[0][0]
        y1 := dots[i][1] - dots[0][1]
        dl := [][]int{}
        for j := 1; j < 4; j++ {
            if i != j { dl = append(dl, dots[j]) }
        }
        x2 := dl[0][0] - dl[1][0]
        y2 := dl[0][1] - dl[1][1]
        if x1*y2 == y1*x2 {
            return 1
        }
    }
    return 0
}