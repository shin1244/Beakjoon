func solution(a int, b int) int {
    if a % 2 == 1 && b % 2 == 1 {
        return a*a + b*b
    } else if a % 2 == 1 || b % 2 == 1 {
        return 2*(a+b)
    }
    if b > a {
        return -(a-b)
    }
    return a-b
}