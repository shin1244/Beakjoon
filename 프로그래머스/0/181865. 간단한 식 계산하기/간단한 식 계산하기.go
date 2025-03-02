import (
    "strings"
    "strconv"
)

func solution(binomial string) int {
    arr := strings.Fields(binomial)
    n1, _ := strconv.Atoi(arr[0]) 
    n2, _ := strconv.Atoi(arr[2]) 
    switch arr[1] {
    case "+":
        return n1 + n2
    case "-":
        return n1 - n2
    case "*":
        return n1 * n2
    }
    return 0
}