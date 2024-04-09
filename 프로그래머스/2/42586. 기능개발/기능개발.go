func solution(progresses []int, speeds []int) []int {
	result := []int{}

	for len(progresses) > 0 {
		cnt := 0
		for idx := range progresses {
			progresses[idx] += speeds[idx]
		}
		for len(progresses) != 0 && progresses[0] >= 100 {
			progresses = progresses[1:]
			speeds = speeds[1:]
			cnt++
		}
		if cnt != 0 {
			result = append(result, cnt)
		}
	}

	return result
}