import "strings"

func solution(myString string) []int {
    strArr:= strings.Split(myString, "x")
    result := []int{}
    for _, val := range strArr {
        result = append(result, len(val))
    }
    return result
}