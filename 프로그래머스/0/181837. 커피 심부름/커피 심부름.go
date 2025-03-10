import "strings"

func solution(order []string) int {
    result := 0
    for _, coffee := range order {
        if strings.Contains(coffee, "cafelatte") {
            result += 5000
        } else {
            result += 4500
        }
    }
    return result
}