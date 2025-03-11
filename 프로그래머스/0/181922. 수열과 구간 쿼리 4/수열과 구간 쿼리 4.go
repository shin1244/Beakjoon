func solution(arr []int, queries [][]int) []int {
    for _, q := range queries {
        for i := q[0]; i <= q[1]; i++ {
            if i % q[2] == 0 {
                arr[i]++
            }
        }
    }
    return arr
}