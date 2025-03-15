func solution(rank []int, attendance []bool) int {
    dict := make(map[int]int)
    result := []int{}
    
    for idx := range rank {
        if attendance[idx] {
            dict[idx] = rank[idx]
        }
    }
    
    for len(result) != 3 {
        temp := -1
        for key, val := range dict {
            if temp == -1 || dict[temp] > val {
                temp = key
            }
        }
        result = append(result, temp)
        delete(dict, temp)
    }
    return result[0] * 10000 + result[1] * 100 + result[2]
}