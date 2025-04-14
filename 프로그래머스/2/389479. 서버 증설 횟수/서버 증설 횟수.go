func solution(players []int, m int, k int) int {
    offTime := []int{}
    maxPlayer := m
    result := 0
    for t, p := range players {
        for len(offTime) != 0 && offTime[0] == t {
            offTime = offTime[1:]
            maxPlayer -= m
        }
        for p >= maxPlayer {
            offTime = append(offTime, t+k)
            maxPlayer += m
            result++
        }
    }
    return result
}