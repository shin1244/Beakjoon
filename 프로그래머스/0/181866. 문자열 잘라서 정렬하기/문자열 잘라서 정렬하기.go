import "sort"

func solution(myString string) []string {
    result := []string{}
    
    temp := ""
    for _, val := range myString {
        if string(val) != "x"  {
            temp += string(val)
        } else if temp != "" {
            result = append(result, temp)
            temp = ""
        }
    }
    if temp != "" {
        result = append(result, temp)
    }
    
    sort.Strings(result)
    return result
}