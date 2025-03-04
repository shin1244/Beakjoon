func solution(arr []int, intervals [][]int) []int {
    result := []int{}
    for idx := range intervals {
        result = append(result,arr[intervals[idx][0]:intervals[idx][1]+1]...)
    }
    return result
}