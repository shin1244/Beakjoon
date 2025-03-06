func solution(my_string string, s int, e int) string {
    temp := []rune(my_string[s:e+1])
    for i, j := 0, len(temp)-1; i < j; i,j = i+1, j-1 {
        temp[i], temp[j] = temp[j], temp[i]
    }
    return my_string[:s] + string(temp) + my_string[e+1:]
}