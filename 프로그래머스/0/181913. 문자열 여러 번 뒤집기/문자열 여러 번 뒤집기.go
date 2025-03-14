func solution(my_string string, queries [][]int) string {
    for _, q := range queries {
        temp := ""
        for i := q[1]; i >= q[0]; i-- {
            temp += string(my_string[i])
        }
        my_string = my_string[:q[0]] + temp + my_string[q[1]+1:]
    }
    return my_string
}