import "strings"

func solution(str_list []string, ex string) string {
    result := ""
    for _, v := range str_list {
        if !strings.Contains(v, ex){
            result += string(v)
        }
    }
    return result
}