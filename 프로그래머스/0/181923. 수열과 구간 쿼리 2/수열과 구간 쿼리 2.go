func solution(arr []int, queries [][]int) []int {
    result := []int{}
    for _, q := range queries {
        temp :=  1000001
        for i := q[0]; i <= q[1]; i++ {
            if temp > arr[i] && q[2] < arr[i] {
                temp = arr[i]
            }
        }
        if temp != 1000001 {
            result = append(result, temp)
        } else {
            result = append(result, -1)
        }
    }
    return result
}