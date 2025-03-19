func solution(s string, skip string, index int) string {
    runes := []rune(s) 
    
    for idx, val := range runes {
        target := val
        
        for i := 0; i < index; {
            target++ 
            if target > 'z' {
                target = 'a'
            }
            check := true
            for _, sp := range skip {
                if target == sp {
                    check = false
                    break
                }
            }
            if check {
                i++
            }
        }
        
        runes[idx] = target
    }
    
    return string(runes)
}