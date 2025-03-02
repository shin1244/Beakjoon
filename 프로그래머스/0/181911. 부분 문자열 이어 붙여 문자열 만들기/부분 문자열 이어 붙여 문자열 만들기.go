import "strings"

func solution(my_strings []string, parts [][]int) string {
    result := []string{}
    
    for i := range parts {
        str := my_strings[i]
        result = append(result, str[parts[i][0]:parts[i][1]+1])
    }
    return strings.Join(result, "")
}