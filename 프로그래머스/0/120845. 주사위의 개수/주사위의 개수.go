func solution(box []int, n int) int {
    x := box[0] / n
    y := box[1] / n
    z := box[2] / n
    return x * y * z
}