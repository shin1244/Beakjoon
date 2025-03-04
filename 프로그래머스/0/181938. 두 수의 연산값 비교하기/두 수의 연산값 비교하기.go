import "strconv"

func solution(a int, b int) int {
    result := 0
    strToInt, _ := strconv.Atoi(strconv.Itoa(a) + strconv.Itoa(b))
    if strToInt > a * b * 2 {
        result = strToInt
    } else {
        result = a * b * 2
    }
    
    return result
}