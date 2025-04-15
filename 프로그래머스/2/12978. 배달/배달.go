func solution(N int, road [][]int, k int) int {
    dist := make([]int, N+1)
    for i := range dist {
        dist[i] = k + 1
    }
    
    q := []int{}
    q = append(q, 1)
    dist[1] = 0
    
    for len(q) > 0 {
        nowNode := q[0]
        q = q[1:]
        
        for _, r := range road {
            if r[0] == nowNode || r[1] == nowNode {
                to, distance := r[1], r[2]
                if r[1] == nowNode {
                    to = r[0]
                }
                if dist[nowNode] + distance < dist[to] {
                    dist[to] = dist[nowNode] + distance
                    q = append(q, to)
                }
            }
        }
    }
    result := 0
    for _, val := range dist {
        if val <= k {
            result++
        }
    }
    return result
}