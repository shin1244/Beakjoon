func solution(arr []int, queries [][]int) []int {
    for _, q := range queries {
        arr[q[0]], arr[q[1]] = arr[q[1]], arr[q[0]]
    }
    return arr
}