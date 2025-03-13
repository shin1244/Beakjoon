func solution(ineq string, eq string, n int, m int) int {
    switch eq {
        case "=":
        if n == m {
            return 1
        }
    }
    switch ineq {
        case "<":
        if n < m {
            return 1
        }
        case ">":
        if n > m {
            return 1
        }
    }
    return 0
}