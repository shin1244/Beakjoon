func solution(myString string, pat string) int {
    result := 0
    patLen:= len(pat)
    for i := 0; i < len(myString) - patLen + 1; i++ {
        if myString[i:i+patLen] == pat {
            result++
        }
    }
    return result
}