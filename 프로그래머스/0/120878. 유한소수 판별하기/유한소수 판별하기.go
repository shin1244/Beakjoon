func gcd(a, b int) int {
    for b != 0 {
        a, b = b, a%b
    }
    return a
}   

func farc(son, mom int) (int, int) {
    g := gcd(son, mom)
    return son / g, mom / g
}

func solution(a int, b int) int {
    a, b = farc(a,b)
    
    for b % 2 == 0 {
        b /= 2
    }
    for b % 5 == 0 {
        b /= 5
    }
    if b == 1 {
        return 1
    }
    return 2
}