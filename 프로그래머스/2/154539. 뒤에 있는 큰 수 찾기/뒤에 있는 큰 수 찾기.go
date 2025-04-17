type idxNum struct {
    idx, num int
}

func solution(numbers []int) []int {
    result := make([]int, len(numbers))
    temp := []idxNum{}
    for idx, num := range numbers {
        for len(temp) > 0 && temp[len(temp)-1].num < num {
            result[temp[len(temp)-1].idx] = num
            temp = temp[:len(temp)-1]
        }
        temp = append(temp, idxNum{idx:idx, num:num})
    }
    
    for _, val := range temp {
        result[val.idx] = -1
    }
    
    return result
}