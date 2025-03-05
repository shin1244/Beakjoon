func solution(arr []int, queries [][]int) []int {
    for _, val := range queries {
        for i := val[0]; i <= val[1]; i++ {
            arr[i]++
        }
    }
    return arr
}