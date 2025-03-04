import "strings"

func solution(strArr []string) []string {
    result := []string{}
    for _, val := range strArr {
        if !strings.Contains(string(val), "ad") {
            result = append(result, string(val))
        }
    }
    return result
}