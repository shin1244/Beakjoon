func BFS(y, x, l int, maps []string) [][]int {
	n := len(maps)
	m := len(maps[0])
	q := [][]int{{0, y, x}}
	visited := make([][]int, n)
	for i := range visited {
		visited[i] = make([]int, m)
	}

	for len(q) > 0 {
		cnt, nowY, nowX := q[0][0], q[0][1], q[0][2]
		q = q[1:]
		if l == 1 && string(maps[nowY][nowX]) == "L" {
			return [][]int{{cnt}, {nowY, nowX}}
		}
		if l == 0 && string(maps[nowY][nowX]) == "E" {
			return [][]int{{cnt}, {nowY, nowX}}
		}
		for _, next := range [][]int{{1, 0}, {-1, 0}, {0, 1}, {0, -1}} {
			nextY, nextX := next[0]+nowY, next[1]+nowX
			nowCnt := cnt + 1
			if 0 <= nextY && nextY < n && 0 <= nextX && nextX < m {
				if string(maps[nextY][nextX]) != "X" && visited[nextY][nextX] == 0 {
					q = append(q, []int{nowCnt, nextY, nextX})
					visited[nextY][nextX] = 1
				}
			}
		}
	}
	return [][]int{{-1}, {-1}}
}

func solution(maps []string) int {
	result := 0
	for y, width := range maps {
		for x, now := range width {
			if now == 'S' {
				bfsResult := BFS(y, x, 1, maps)
				if bfsResult[0][0] == -1 {
					return -1
				}
				result += bfsResult[0][0]
				bfsResult = BFS(bfsResult[1][0], bfsResult[1][1], 0, maps)
				if bfsResult[0][0] == -1 {
					return -1
				}
				result += bfsResult[0][0]
				return result
			}
		}
	}
	return -1
}