import "strconv"

func solution(number string) int {
    n := 0
    for _, v := range number {
        a, _ := strconv.Atoi(string(v))
        n += a
    }
    return n%9
}