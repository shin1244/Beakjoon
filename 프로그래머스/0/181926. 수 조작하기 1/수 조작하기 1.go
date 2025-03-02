func solution(n int, control string) int {
    for _, val := range control {
        switch val {
            case 'w':
            n++
            case 's':
            n--
            case 'd':
            n+=10
            case 'a':
            n-=10
        }
    }
    return n
}