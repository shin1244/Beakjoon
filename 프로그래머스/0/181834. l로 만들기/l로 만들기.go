func solution(myString string) string {
    result := ""

    for _, ch := range myString { 
        if ch < 'l' { 
            result += "l" 
        } else {
            result += string(ch)
        }
    }
    
    return result
}
