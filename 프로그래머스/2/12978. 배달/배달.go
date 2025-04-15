import (
    "container/heap"
)

type Item struct {
    node, distance int
}

type PriorityQueue []Item

func (pq PriorityQueue) Len() int { return len(pq) }
func (pq PriorityQueue) Less(i, j int) bool { return pq[i].distance < pq[j].distance }
func (pq PriorityQueue) Swap(i, j int) { pq[i], pq[j] = pq[j], pq[i] }
func (pq *PriorityQueue) Push(x interface{}) {
    *pq = append(*pq, x.(Item))
}
func (pq *PriorityQueue) Pop() interface{} {
    old := *pq
    element := old[len(old)-1]
    *pq = old[0:len(old)-1]
    return element
}

func solution(N int, road [][]int, k int) int {
    dist := make([]int, N + 1)
    for i := range dist {
        dist[i] = k + 1
    }
    dist[1] = 0
    
    graph := make(map[int][]Item)
    for _, r := range road {
        start, end, distance := r[0], r[1], r[2]
        graph[start] = append(graph[start], Item{node: end, distance:distance})
        graph[end] = append(graph[end], Item{node: start, distance:distance})
    }
    
    pq := &PriorityQueue{}
    heap.Init(pq)
    heap.Push(pq, Item{node:1, distance:0})
    for pq.Len() > 0 {
        nowNode := pq.Pop().(Item)
        for _, item := range graph[nowNode.node] {
            if dist[item.node] > nowNode.distance + item.distance {
                dist[item.node] = nowNode.distance + item.distance
                heap.Push(pq, Item{node:item.node, distance:nowNode.distance + item.distance})
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