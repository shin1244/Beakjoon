import "strings"

func solution(myString string, pat string) int {
    patRunes := []rune(pat)

    for i, ch := range patRunes {
        if ch == 'A' {
            patRunes[i] = 'B'
        } else if ch == 'B' {
            patRunes[i] = 'A'
        }
    }

    newPat := string(patRunes)

    if strings.Contains(myString, newPat) {
        return 1
    }
    return 0
}