func solution(num_list []int) []int {
    for i := 1; i < len(num_list); i++ {
        key := num_list[i]
        j := i - 1
        for j >= 0 && num_list[j] > key {
            num_list[j+1] = num_list[j]
            j--
        }
        num_list[j+1] = key
    }
    return num_list[5:]
}