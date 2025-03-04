func solution(n int) int {
    result := 0
    
    for i := 4; i <= n; i++ {
        c := false
        for j := 2; j * j <= i; j++{
            if i % j == 0 {
                c = true
            }
        }
        if c {
            result++
        }
    }
    return result
}