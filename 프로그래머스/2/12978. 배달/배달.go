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
    dist := make([]int, N+1)
    for i := 2; i < N+1; i++ {
        dist[i] = int(1e9)
    }
    graph := make(map[int][]Item)
    for _, r := range road {
        from, to, distance := r[0], r[1], r[2]
        graph[from] = append(graph[from], Item{node: to, distance: distance})
        graph[to] = append(graph[to], Item{node: from, distance: distance})
    }
    
    pq := &PriorityQueue{}
    heap.Init(pq)
    heap.Push(pq, Item{node:1, distance:0})
    
    for pq.Len() > 0 {
        nowItem := heap.Pop(pq).(Item)
        if nowItem.distance > dist[nowItem.node] {
            continue
        }
        for _, edge := range graph[nowItem.node] {
            newDist := dist[nowItem.node] + edge.distance
            if newDist < dist[edge.node] {
                dist[edge.node] = newDist
                heap.Push(pq, Item{node:edge.node, distance:newDist})
            }
        }
    }
    result := 0
    for _, val := range dist {
        if val != 0 && val <= k {
            result++
        }
    }
    return result+1
}