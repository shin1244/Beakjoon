import "strconv"

func solution(num_list []int) int {
    odd := ""
    even := ""
    for _, val := range num_list {
        if val % 2 == 1 {
            odd += strconv.Itoa(val)
        } else {
            even += strconv.Itoa(val)
        }
    }
    oddNum, _:= strconv.Atoi(odd)
    evenNum, _ := strconv.Atoi(even)
    return oddNum + evenNum
}