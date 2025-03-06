func solution(myString string, pat string) string {
    patLen := len(pat)
    for i := len(myString); i >= patLen; i-- {
        temp := myString[:i]
        if temp[len(temp)-patLen:] == pat{
            return temp
        }
    }
    return ""
}